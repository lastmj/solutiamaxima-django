# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categories'
        db.create_table(u'publicworkspace_categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parentCategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publicworkspace.Categories'], null=True, blank=True)),
        ))
        db.send_create_signal(u'publicworkspace', ['Categories'])


    def backwards(self, orm):
        # Deleting model 'Categories'
        db.delete_table(u'publicworkspace_categories')


    models = {
        u'publicworkspace.categories': {
            'Meta': {'object_name': 'Categories'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publicworkspace.Categories']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['publicworkspace']