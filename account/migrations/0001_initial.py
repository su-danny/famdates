# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'InterestCategory'
        db.create_table('account_interestcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('human_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('account', ['InterestCategory'])

        # Adding model 'Interest'
        db.create_table('account_interest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.InterestCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('account', ['Interest'])

        # Adding model 'UserProfile'
        db.create_table('account_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_profile', unique=True,
                                                                           to=orm['auth.User'])),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('acct_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('about_me', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('use_gravatar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_founded', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('profile_type',
             self.gf('django.db.models.fields.CharField')(default='normal', max_length=20, null=True, blank=True)),
            ('facebook_uid', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('default_interest_feed',
             self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.InterestCategory'], null=True,
                                                                   blank=True)),
        ))
        db.send_create_signal('account', ['UserProfile'])

        # Adding M2M table for field fan_zone_interests on 'UserProfile'
        db.create_table('account_userprofile_fan_zone_interests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['account.userprofile'], null=False)),
            ('interest', models.ForeignKey(orm['account.interest'], null=False))
        ))
        db.create_unique('account_userprofile_fan_zone_interests', ['userprofile_id', 'interest_id'])

        # Adding M2M table for field fitness_nutrition_interests on 'UserProfile'
        db.create_table('account_userprofile_fitness_nutrition_interests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['account.userprofile'], null=False)),
            ('interest', models.ForeignKey(orm['account.interest'], null=False))
        ))
        db.create_unique('account_userprofile_fitness_nutrition_interests', ['userprofile_id', 'interest_id'])

        # Adding M2M table for field game_time_interests on 'UserProfile'
        db.create_table('account_userprofile_game_time_interests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['account.userprofile'], null=False)),
            ('interest', models.ForeignKey(orm['account.interest'], null=False))
        ))
        db.create_unique('account_userprofile_game_time_interests', ['userprofile_id', 'interest_id'])

        # Adding model 'FacebookSession'
        db.create_table('account_facebooksession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=103)),
            ('expires', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('uid', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True)),
        ))
        db.send_create_signal('account', ['FacebookSession'])

        # Adding unique constraint on 'FacebookSession', fields ['user', 'uid']
        db.create_unique('account_facebooksession', ['user_id', 'uid'])

        # Adding unique constraint on 'FacebookSession', fields ['access_token', 'expires']
        db.create_unique('account_facebooksession', ['access_token', 'expires'])

        # Adding model 'MailingAddress'
        db.create_table('account_mailingaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('account', ['MailingAddress'])


    def backwards(self, orm):
        # Removing unique constraint on 'FacebookSession', fields ['access_token', 'expires']
        db.delete_unique('account_facebooksession', ['access_token', 'expires'])

        # Removing unique constraint on 'FacebookSession', fields ['user', 'uid']
        db.delete_unique('account_facebooksession', ['user_id', 'uid'])

        # Deleting model 'InterestCategory'
        db.delete_table('account_interestcategory')

        # Deleting model 'Interest'
        db.delete_table('account_interest')

        # Deleting model 'UserProfile'
        db.delete_table('account_userprofile')

        # Removing M2M table for field fan_zone_interests on 'UserProfile'
        db.delete_table('account_userprofile_fan_zone_interests')

        # Removing M2M table for field fitness_nutrition_interests on 'UserProfile'
        db.delete_table('account_userprofile_fitness_nutrition_interests')

        # Removing M2M table for field game_time_interests on 'UserProfile'
        db.delete_table('account_userprofile_game_time_interests')

        # Deleting model 'FacebookSession'
        db.delete_table('account_facebooksession')

        # Deleting model 'MailingAddress'
        db.delete_table('account_mailingaddress')


    models = {
        'account.facebooksession': {
            'Meta': {'unique_together': "(('user', 'uid'), ('access_token', 'expires'))",
                     'object_name': 'FacebookSession'},
            'access_token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '103'}),
            'expires': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'account.interest': {
            'Meta': {'object_name': 'Interest'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.InterestCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.interestcategory': {
            'Meta': {'object_name': 'InterestCategory'},
            'human_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'account.mailingaddress': {
            'Meta': {'object_name': 'MailingAddress'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_2': (
            'django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'acct_type': (
            'django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'avatar': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_founded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'default_interest_feed': ('django.db.models.fields.related.ForeignKey', [],
                                      {'to': "orm['account.InterestCategory']", 'null': 'True', 'blank': 'True'}),
            'facebook_uid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fan_zone_interests': ('django.db.models.fields.related.ManyToManyField', [],
                                   {'blank': 'True', 'related_name': "'fan_zone'", 'null': 'True',
                                    'symmetrical': 'False', 'to': "orm['account.Interest']"}),
            'fitness_nutrition_interests': ('django.db.models.fields.related.ManyToManyField', [],
                                            {'blank': 'True', 'related_name': "'fitness_nutrition'", 'null': 'True',
                                             'symmetrical': 'False', 'to': "orm['account.Interest']"}),
            'game_time_interests': ('django.db.models.fields.related.ManyToManyField', [],
                                    {'blank': 'True', 'related_name': "'game_time'", 'null': 'True',
                                     'symmetrical': 'False', 'to': "orm['account.Interest']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': (
            'django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'profile_type': ('django.db.models.fields.CharField', [],
                             {'default': "'normal'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'use_gravatar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [],
                     {'related_name': "'user_profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        },
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
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['account']