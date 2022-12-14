# Generated by Django 4.1 on 2022-08-20 15:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
        ('coltrane', '0002_auto_20220820_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('excerpt', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('enable_comments', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique_for_date='pub_date')),
                ('status', models.IntegerField(choices=[(1, 'Live'), (2, 'Draft'), (3, 'Hidden')], default=1)),
                ('excerpt_html', models.TextField(blank=True, editable=False)),
                ('body_html', models.TextField(blank=True, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='coltrane.category')),
                ('tags', taggit.managers.TaggableManager(help_text='Separate tags with spaces', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'ordering': ['-pub_date'],
            },
        ),
    ]
