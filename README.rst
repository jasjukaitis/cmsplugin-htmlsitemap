cmsplugin-htmlsitemap
=====================

This is an HTML sitemap plugin for Django CMS.

Requirements
============

  * Django
  * django-cms

Installation
============

Using pip to install the plugin::

  pip install cmsplugin-htmlsitemap

Configuration
=============

Add ``cmsplugin_htmlsitemap`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

After adding the CMS plugin you can filter listed pages by their:

  * starting/minimal level
  * deepest/maximal level
  * is in navigation
  * exact match on created by
  * match title containing substring
  * URL match with regular expression

