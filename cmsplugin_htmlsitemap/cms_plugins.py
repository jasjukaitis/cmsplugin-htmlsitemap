# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from cms.models.pagemodel import Page
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_htmlsitemap import models
import re


class HtmlSitemapPlugin(CMSPluginBase):
    """HTML Sitemap CMS plugin."""

    name = _('HTML Sitemap')
    model = models.HtmlSitemap
    render_template = 'cmsplugin_htmlsitemap/sitemap.html'

    def render(self, context, instance, placeholder):
        site = Site.objects.get_current()
        pages = Page.objects.published(site=site).order_by('tree_id', 'lft')
        pages = pages.filter(level__gte=instance.level_min, level__lte=instance.level_max)
        if not instance.in_navigation is None:
            pages = pages.filter(in_navigation=instance.in_navigation)
        if instance.match_created_by:
            pages = pages.filter(created_by=instance.match_created_by)
        if instance.match_title:
            pages = pages.filter(title_set__title__contains=instance.match_title)
        if instance.match_url:
            pat = re.compile(instance.match_url, re.IGNORECASE)
            pages = [ p  for p in pages if pat.search(p.get_absolute_url()) ]
        context.update({
            'instance':instance,
            'pages':pages,
        })
        return context

plugin_pool.register_plugin(HtmlSitemapPlugin)

