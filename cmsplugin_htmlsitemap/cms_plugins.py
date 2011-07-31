# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from cms.models.pagemodel import Page
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

class HtmlSitemapPlugin(CMSPluginBase):
    name = _('HTML Sitemap')
    render_template = 'cmsplugin_htmlsitemap/sitemap.html'

    def render(self, context, instance, placeholder):
        pages = Page.tree.filter(published=True)
        context.update(
            {'instance': instance,
             'pages': pages
            }
        )
        return context

plugin_pool.register_plugin(HtmlSitemapPlugin)
