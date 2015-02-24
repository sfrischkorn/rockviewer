# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sample.erb101_sample'
        db.add_column(u'three_d_viewer_sample', 'erb101_sample',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sample.erb101_sample'
        db.delete_column(u'three_d_viewer_sample', 'erb101_sample')


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
        u'three_d_viewer.glossaryentry': {
            'Meta': {'object_name': 'GlossaryEntry'},
            'definition': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'three_d_viewer.mineral': {
            'Meta': {'object_name': 'Mineral', '_ormbases': [u'three_d_viewer.Sample']},
            'chemical_formula': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cleavage_fracture': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'crystallography': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'habit': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
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
            'erb101_sample': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_filename': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'samples'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['three_d_viewer.Category']"}),
            'viewed_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['three_d_viewer']