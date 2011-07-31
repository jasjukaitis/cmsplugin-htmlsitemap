from setuptools import setup
import os

setup(
    name='cmsplugin-htmlsitemap',
    version='0.1.0',
    description='HTML sitemap plugin for Django CMS',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Raphael Jasjukaitis',
    author_email='webmaster@raphaa.de',
    url='https://github.com/raphaa/cmsplugin-htmlsitemap',
    packages = [
        "cmsplugin_htmlsitemap",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False
)