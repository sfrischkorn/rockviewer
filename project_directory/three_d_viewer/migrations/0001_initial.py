# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'three_d_viewer_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, on_delete=models.SET_NULL, to=orm['three_d_viewer.Category'])),
        ))
        db.send_create_signal(u'three_d_viewer', ['Category'])

        # Adding model 'Sample'
        db.create_table(u'three_d_viewer_sample', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('model_filename', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['three_d_viewer.Category'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'three_d_viewer', ['Sample'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'three_d_viewer_category')

        # Deleting model 'Sample'
        db.delete_table(u'three_d_viewer_sample')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_filename': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['three_d_viewer.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        }
    }

    complete_apps = ['three_d_viewer']