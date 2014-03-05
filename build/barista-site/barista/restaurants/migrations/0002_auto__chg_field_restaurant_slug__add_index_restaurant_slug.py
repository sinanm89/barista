# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Restaurant.slug'
        db.alter_column(u'restaurants_restaurant', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255))
        # Adding index on 'Restaurant', fields ['slug']
        db.create_index(u'restaurants_restaurant', ['slug'])


    def backwards(self, orm):
        # Removing index on 'Restaurant', fields ['slug']
        db.delete_index(u'restaurants_restaurant', ['slug'])


        # Changing field 'Restaurant.slug'
        db.alter_column(u'restaurants_restaurant', 'slug', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'restaurants.restaurant': {
            'Meta': {'ordering': "['name']", 'object_name': 'Restaurant'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'category'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['restaurants.RestaurantCategory']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Restaurant'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'restaurant'", 'max_length': '255'}),
            'times_chosen': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'restaurants.restaurantcategory': {
            'Meta': {'ordering': "['order', '-id']", 'object_name': 'RestaurantCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'times_chosen': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['restaurants']