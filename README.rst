cmsplugin-htmlsitemap
=====================

This is an HTML sitemap plugin for Django CMS (3).

Requirements
============

  * Django
  * django-cms

Installation
============

Using PyPI you can simply type into a terminal:

    pip install cmsplugin-htmlsitemap

or

    easy_install cmsplugin-htmlsitemap

Configuration
=============

Add ``cmsplugin_htmlsitemap`` to the list of ``INSTALLED_APPS`` in your
``settings.py`` file. Don't forget to syncdb your database or migrate if you're
using ``south``.

After adding the CMS plugin you can configure filtering of listed pages by their::

  * starting/minimal level
  * deepest/maximal level
  * is in navigation
  * exact match on created by
  * match title containing substring
  * URL match with regular expression
  * pages in the current language


Author
======

Copyright 2011-2014 Raphael Jasjukaitis <hello@raphael-jasjukaitis.de>


Contributors
============

  * gw0 <gw.2011@tnode.com or http://gw.tnode.com/>
  * mihaisucan
  * abrown1982
  * acspike


Released under the BSD license.
