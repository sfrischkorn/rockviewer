# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Mineral.specific_gravity'
        db.alter_column(u'three_d_viewer_mineral', 'specific_gravity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2))

        # Changing field 'Mineral.hardness'
        db.alter_column(u'three_d_viewer_mineral', 'hardness', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Mineral.specific_gravity'
        db.alter_column(u'three_d_viewer_mineral', 'specific_gravity', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=2))

        # Changing field 'Mineral.hardness'
        db.alter_column(u'three_d_viewer_mineral', 'hardness', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=2))

    models = {
        u'three_d_viewer.answer': {
            'Meta': {'object_name': 'Answer'},
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['three_d_viewer.Question']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'three_d_viewer.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['three_d_viewer.Category']"})
        },
        u'three_d_viewer.mineral': {
            'Meta': {'object_name': 'Mineral', '_ormbases': [u'three_d_viewer.Sample']},
            'chemical_formula': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cleavage_fracture': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'crystallography': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'habit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'hardness': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'}),
            'identifying_features': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'lustre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'occurance': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            u'sample_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['three_d_viewer.Sample']", 'unique': 'True', 'primary_key': 'True'}),
            'specific_gravity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'streak': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'three_d_viewer.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sample': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': u"orm['three_d_viewer.Sample']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'three_d_viewer.sample': {
            'Meta': {'object_name': 'Sample'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_filename': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'samples'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['three_d_viewer.Category']"})
        }
    }

    complete_apps = ['three_d_viewer']