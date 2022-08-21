from django.db import models
from django.contrib.auth.models import User
import datetime
from markdown import markdown
from taggit.managers import TaggableManager

class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from title. Must be unique.')
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    class Admin:
        pass

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug
    
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
        return "/weblog/%s/%s" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
