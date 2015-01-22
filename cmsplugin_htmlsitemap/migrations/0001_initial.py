# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlSitemap',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('level_min', models.PositiveSmallIntegerField(default=0, verbose_name='starting level')),
                ('level_max', models.PositiveSmallIntegerField(default=100, verbose_name='deepest level')),
                ('in_navigation', models.NullBooleanField(default=None, verbose_name='is in navigation')),
                ('match_created_by', models.CharField(max_length=70, verbose_name='exact match on created by', blank=True)),
                ('match_title', models.CharField(max_length=255, verbose_name='match title containing substring', blank=True)),
                ('match_url', models.CharField(max_length=100, verbose_name='URL match with regular expression', blank=True)),
                ('match_language', models.BooleanField(default=False, verbose_name='match only pages in current language')),
            ],
            options={
                'ordering': ('level_min', 'level_max'),
                'verbose_name': 'HTML Sitemap plugin',
                'verbose_name_plural': 'HTML Sitemap plugins',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
