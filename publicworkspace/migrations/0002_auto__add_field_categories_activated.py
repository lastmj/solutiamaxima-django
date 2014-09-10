# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Categories.activated'
        db.add_column(u'publicworkspace_categories', 'activated',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Categories.activated'
        db.delete_column(u'publicworkspace_categories', 'activated')


    models = {
        u'publicworkspace.categories': {
            'Meta': {'object_name': 'Categories'},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publicworkspace.Categories']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['publicworkspace']