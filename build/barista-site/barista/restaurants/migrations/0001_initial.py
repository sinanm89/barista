# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table(u'restaurants_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Restaurant', max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='Restaurant', max_length=255)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('times_chosen', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'restaurants', ['Restaurant'])

        # Adding M2M table for field category on 'Restaurant'
        db.create_table(u'restaurants_restaurant_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm[u'restaurants.restaurant'], null=False)),
            ('restaurantcategory', models.ForeignKey(orm[u'restaurants.restaurantcategory'], null=False))
        ))
        db.create_unique(u'restaurants_restaurant_category', ['restaurant_id', 'restaurantcategory_id'])

        # Adding model 'RestaurantCategory'
        db.create_table(u'restaurants_restaurantcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('times_chosen', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'restaurants', ['RestaurantCategory'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table(u'restaurants_restaurant')

        # Removing M2M table for field category on 'Restaurant'
        db.delete_table('restaurants_restaurant_category')

        # Deleting model 'RestaurantCategory'
        db.delete_table(u'restaurants_restaurantcategory')


    models = {
        u'restaurants.restaurant': {
            'Meta': {'ordering': "['name']", 'object_name': 'Restaurant'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'category'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['restaurants.RestaurantCategory']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Restaurant'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "'Restaurant'", 'max_length': '255'}),
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