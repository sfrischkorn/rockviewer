# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sample.description'
        db.add_column(u'three_d_viewer_sample', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sample.description'
        db.delete_column(u'three_d_viewer_sample', 'description')


    models = {
        u'three_d_viewer.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['three_d_viewer.Category']"})
        },
        u'three_d_viewer.sample': {
            'Meta': {'object_name': 'Sample'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_filename': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['three_d_viewer.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        }
    }

    complete_apps = ['three_d_viewer']