# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HtmlSitemap'
        db.create_table('cmsplugin_htmlsitemap', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('level_min', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('level_max', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=100)),
            ('in_navigation', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('match_created_by', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('match_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('match_url', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('cmsplugin_htmlsitemap', ['HtmlSitemap'])


    def backwards(self, orm):
        
        # Deleting model 'HtmlSitemap'
        db.delete_table('cmsplugin_htmlsitemap')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_htmlsitemap.htmlsitemap': {
            'Meta': {'ordering': "('level_min', 'level_max')", 'object_name': 'HtmlSitemap', 'db_table': "'cmsplugin_htmlsitemap'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'level_max': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'level_min': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'match_created_by': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'match_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'match_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_htmlsitemap']
