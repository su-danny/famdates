# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting field 'Card.address_city'
        db.delete_column('tiger_card', 'address_city')

        # Adding field 'Card.address_country'
        db.add_column('tiger_card', 'address_country',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Card.address_line2'
        db.alter_column('tiger_card', 'address_line2',
                        self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Card.address_line1'
        db.alter_column('tiger_card', 'address_line1',
                        self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Card.address_state'
        db.alter_column('tiger_card', 'address_state',
                        self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Card.address_zip'
        db.alter_column('tiger_card', 'address_zip',
                        self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

    def backwards(self, orm):
        # User chose to not deal with backwards NULL issues for 'Card.address_city'
        raise RuntimeError("Cannot reverse this migration. 'Card.address_city' and its values cannot be restored.")
        # Deleting field 'Card.address_country'
        db.delete_column('tiger_card', 'address_country')


        # User chose to not deal with backwards NULL issues for 'Card.address_line2'
        raise RuntimeError("Cannot reverse this migration. 'Card.address_line2' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Card.address_line1'
        raise RuntimeError("Cannot reverse this migration. 'Card.address_line1' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Card.address_state'
        raise RuntimeError("Cannot reverse this migration. 'Card.address_state' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Card.address_zip'
        raise RuntimeError("Cannot reverse this migration. 'Card.address_zip' and its values cannot be restored.")

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
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tiger.Customer']"}),
            'exp_month': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'exp_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'fingerprint': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'tiger.customer': {
            'Meta': {'object_name': 'Customer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['tiger']