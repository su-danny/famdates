# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Child'
        db.create_table('account_child', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent', to=orm['account.UserProfile'])),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('interest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.InterestCategory'], null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('account', ['Child'])


    def backwards(self, orm):
        # Deleting model 'Child'
        db.delete_table('account_child')


    models = {
        'account.child': {
            'Meta': {'object_name': 'Child'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.InterestCategory']", 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent'", 'to': "orm['account.UserProfile']"})
        },
        'account.eventjoin': {
            'Meta': {'object_name': 'EventJoin'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.UserProfile']"})
        },
        'account.facebooksession': {
            'Meta': {'unique_together': "(('user', 'uid'), ('access_token', 'expires'))", 'object_name': 'FacebookSession'},
            'access_token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '103'}),
            'expires': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'account.interest': {
            'Meta': {'object_name': 'Interest'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.InterestCategory']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.InterestGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_category': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'account.interestcategory': {
            'Meta': {'object_name': 'InterestCategory'},
            'human_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.interestgroup': {
            'Meta': {'object_name': 'InterestGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.mailingaddress': {
            'Meta': {'object_name': 'MailingAddress'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'acct_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'attn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'background_cropped': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'blocked_users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'current_registration_step': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'date_founded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deactivated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default_interest_feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.InterestCategory']", 'null': 'True', 'blank': 'True'}),
            'email_notification': ('django.db.models.fields.CharField', [], {'default': "'enabled'", 'max_length': '50'}),
            'facebook_uid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fan_zone_interests': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fan_zone'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['account.Interest']"}),
            'fitness_nutrition_interests': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fitness_nutrition'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['account.Interest']"}),
            'game_time_interests': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'game_time'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['account.Interest']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'hide_birthday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joined_events': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'joined_userprofile'", 'to': "orm['events.Event']", 'through': "orm['account.EventJoin']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'profile_type': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'receive_email_for_new_message': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'receive_email_from_groups': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_month_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'stats': ('picklefield.fields.PickledObjectField', [], {'null': 'True'}),
            'use_gravatar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_profile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'beginning': ('django.db.models.fields.DateField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'duration': ('durationfield.db.models.fields.duration.DurationField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.SmallIntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Interest']", 'symmetrical': 'False'}),
            'interval': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "'Unknown Event'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'repetitions': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'pub'", 'max_length': '3'})
        }
    }

    complete_apps = ['account']