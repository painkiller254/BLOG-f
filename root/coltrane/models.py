from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from markdown import markdown
from taggit.managers import TaggableManager
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from title. Must be unique.')
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    class Admin:
        pass

    def live_enrty_set(self):
        from coltrane.models import Entry
        return self.entry_set.filter(status=Entry.LIVE_STATUS)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

    
class LiveEntryManager(models.Manager):
        def get_query_set(self):
            return super(LiveEntryManager, self).get_quey_set().filter(status=self.model.LIVE_STATUS)


class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS =2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden')
    )

    # Core fields
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Metadata
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    # Fields to store generated HTML
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    # Categorization
    categories = models.ManyToManyField(Category)
    tags = TaggableManager(help_text="Separate tags with spaces")

    live = LiveEntryManager()
    objets = models.Manager()

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']

    class Admin:
        pass

   

    def __unicode__(self):
        return self.title

    def save(self):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.exerpt_html = markdown(self.excerpt)
        super(Entry, self).save()
        # this function runs markdown over the body field and stores the resulting HTML in body_html

    def get_absolute_url(self):
        return reverse('coltrane_entry_detail', (), {'year': self.pub_date.strftime("%Y"), 'month': self.pub_date.strftime("%b").lower(), 'day': self.pub_date.strftime("%d"), 'slug': self.slug })
    

class Link(models.Model):
    # metadata
    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to del.icio.us', default=True, help_text='If hecked, this link will be posted both to your weblog and to your del.icio.us account.')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField( unique_for_date='pub_date', help_text='Must be unique for the publication date.')
    title = models.CharField(max_length=250)

    # actula link bits.
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    via_name = models.CharField('Via', max_length=250, blank=True, help_text="The name of the person whose site you spotted the link on. Optional.")
    via_url = models.URLField('Via URL', blank=True, help_text='The URL of the site where you spotted the link. Optional.')
    tags = TaggableManager()
    url = models.URLField('URL', unique=True)

    class Meta:
        ordering = ['-pub_date']

    class Admin:
        pass

    def __unicode__(self):
        return self.title

    def save(self):
        if self.description:
            self.description_html = markdown(self.description)
        if not self.id and self.post_elsewhere:
            import pydelicious
            from django.utils.encoding import smart_str
            pydelicious.add(settings.DELICIOUS_USER, settings.DELICIOUS_PASSWORD, smart_str(self.url), smart_str(self.title), smart_str(self.tags))
        super(Link, self).save()

    def get_absolute_url(self):
        return reverse('coltrane_link_detail', (), { 'year': self.pub_date.strftime('%Y'), 'month': self.pub_date.strftime('%b').lower(), 'day': self.pub_date.strftime('%d'), 'slug': self.slug })
    
