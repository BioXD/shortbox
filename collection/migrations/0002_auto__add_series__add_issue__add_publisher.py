# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Series'
        db.create_table('collection_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('volume', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.Publisher'])),
        ))
        db.send_create_signal('collection', ['Series'])

        # Adding model 'Issue'
        db.create_table('collection_issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.Series'])),
            ('pub_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('collection', ['Issue'])

        # Adding model 'Publisher'
        db.create_table('collection_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection.Publisher'], null=True, blank=True)),
        ))
        db.send_create_signal('collection', ['Publisher'])


    def backwards(self, orm):
        # Deleting model 'Series'
        db.delete_table('collection_series')

        # Deleting model 'Issue'
        db.delete_table('collection_issue')

        # Deleting model 'Publisher'
        db.delete_table('collection_publisher')


    models = {
        'collection.issue': {
            'Meta': {'object_name': 'Issue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Series']"})
        },
        'collection.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Publisher']", 'null': 'True', 'blank': 'True'})
        },
        'collection.series': {
            'Meta': {'object_name': 'Series'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collection.Publisher']"}),
            'volume': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['collection']