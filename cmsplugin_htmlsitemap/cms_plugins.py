# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _

from cms.models.pagemodel import Page
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

class HtmlSitemapPlugin(CMSPluginBase):
    name = _('HTML Sitemap')
    render_template = 'cmsplugin_htmlsitemap/sitemap.html'

    def render(self, context, instance, placeholder):
        site = Site.objects.get_current()
        pages = Page.objects.published(site=site).order_by('tree_id', 'lft')
        context.update(
            {'instance': instance,
             'pages': pages
            }
        )
        return context

plugin_pool.register_plugin(HtmlSitemapPlugin)
