# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Invoice'
        db.create_table('tiger_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('submitted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('charge_id', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('charge_attempts', self.gf('django.db.models.fields.TextField')()),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tiger.Card'])),
        ))
        db.send_create_signal('tiger', ['Invoice'])

        # Deleting field 'Customer.stripe_id'
        db.delete_column('tiger_customer', 'stripe_id')

        # Deleting field 'Card.customer'
        db.delete_column('tiger_card', 'customer_id')

        # Adding field 'Card.stripe_id'
        db.add_column('tiger_card', 'stripe_id',
                      self.gf('django.db.models.fields.CharField')(default='NONE', max_length=25),
                      keep_default=False)

        # Adding field 'Card.user'
        db.add_column('tiger_card', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='credit_cards',
                                                                            to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Invoice'
        db.delete_table('tiger_invoice')


        # User chose to not deal with backwards NULL issues for 'Customer.stripe_id'
        raise RuntimeError("Cannot reverse this migration. 'Customer.stripe_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Card.customer'
        raise RuntimeError("Cannot reverse this migration. 'Card.customer' and its values cannot be restored.")
        # Deleting field 'Card.stripe_id'
        db.delete_column('tiger_card', 'stripe_id')

        # Deleting field 'Card.user'
        db.delete_column('tiger_card', 'user_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [],
                            {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')",
                     'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': (
            'django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tiger.card': {
            'Meta': {'object_name': 'Card'},
            'address_country': (
            'django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_line1': (
            'django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_line2': (
            'django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_state': (
            'django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'address_zip': (
            'django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'exp_month': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'exp_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'fingerprint': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'user': ('django.db.models.fields.related.ForeignKey', [],
                     {'related_name': "'credit_cards'", 'to': "orm['auth.User']"})
        },
        'tiger.customer': {
            'Meta': {'object_name': 'Customer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'tiger.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tiger.Card']"}),
            'charge_attempts': ('django.db.models.fields.TextField', [], {}),
            'charge_id': (
            'django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submitted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tiger']