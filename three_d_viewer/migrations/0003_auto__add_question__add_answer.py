# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'three_d_viewer_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('sample', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['three_d_viewer.Sample'])),
        ))
        db.send_create_signal(u'three_d_viewer', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'three_d_viewer_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['three_d_viewer.Question'])),
        ))
        db.send_create_signal(u'three_d_viewer', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'three_d_viewer_question')

        # Deleting model 'Answer'
        db.delete_table(u'three_d_viewer_answer')


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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['three_d_viewer.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        }
    }

    complete_apps = ['three_d_viewer']