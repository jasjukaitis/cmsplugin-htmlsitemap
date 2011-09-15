# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class HtmlSitemap(CMSPlugin):
    """Model for HTML Sitemap CMS plugin."""

    level_min = models.PositiveSmallIntegerField(_('starting level'), default=0)
    level_max = models.PositiveSmallIntegerField(_('deepest level'), default=100)
    in_navigation = models.NullBooleanField(_('is in navigation'), default=None)
    match_created_by = models.CharField(_('exact match on created by'), blank=True,
        max_length=70)
    match_title = models.CharField(_('match title containing substring'), blank=True,
        max_length=255)
    match_url = models.CharField(_('URL match with regular expression'), blank=True,
        max_length=100)

    class Meta:
        verbose_name = _('HTML Sitemap plugin')
        verbose_name_plural = _('HTML Sitemap plugins')
        ordering = ('level_min', 'level_max')

    def __unicode__(self):
        return u'HTML Sitemap {0}-{1}'.format(self.level_min, self.level_max)

