# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

ABR_STATE_CHOICES = (('', ''), ('AL', 'AL'), ('AK', 'AK'), ('AS', 'AS'), ('AZ', 'AZ'), ('AR', 'AR'), ('AA', 'AA'),
                     ('AE', 'AE'), ('AP', 'AP'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'),
                     ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('GU', 'GU'), ('HI', 'HI'), ('ID', 'ID'),
                     ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'),
                     ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'),
                     ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'),
                     ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('MP', 'MP'), ('OH', 'OH'),
                     ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('PR', 'PR'), ('RI', 'RI'), ('SC', 'SC'),
                     ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VI', 'VI'),
                     ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY'))

#class Country(models.Model):
#    code = models.CharField(max_length=9, primary_key=True, db_column='Code')  # Field name made lowercase.
#    name = models.CharField(max_length=156, db_column='Name')  # Field name made lowercase.
#    continent = models.CharField(max_length=39, db_column='Continent')  # Field name made lowercase.
#    region = models.CharField(max_length=78, db_column='Region')  # Field name made lowercase.
#    surfacearea = models.FloatField(db_column='SurfaceArea')  # Field name made lowercase.
#    indepyear = models.IntegerField(null=True, db_column='IndepYear', blank=True)  # Field name made lowercase.
#    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
#    lifeexpectancy = models.FloatField(null=True, db_column='LifeExpectancy', blank=True)  # Field name made lowercase.
#    gnp = models.FloatField(null=True, db_column='GNP', blank=True)  # Field name made lowercase.
#    gnpold = models.FloatField(null=True, db_column='GNPOld', blank=True)  # Field name made lowercase.
#    localname = models.CharField(max_length=135, db_column='LocalName')  # Field name made lowercase.
#    governmentform = models.CharField(max_length=135, db_column='GovernmentForm')  # Field name made lowercase.
#    headofstate = models.CharField(max_length=180, db_column='HeadOfState', blank=True)  # Field name made lowercase.
#    capital = models.IntegerField(null=True, db_column='Capital', blank=True)  # Field name made lowercase.
#    code2 = models.CharField(max_length=6, db_column='Code2')  # Field name made lowercase.
#    class Meta:
#        db_table = u'Country'
#
#class Countrylanguage(models.Model):
#    countrycode = models.ForeignKey(Country, db_column='CountryCode')  # Field name made lowercase.
#    language = models.CharField(max_length=90, primary_key=True, db_column='Language')  # Field name made lowercase.
#    isofficial = models.CharField(max_length=3, db_column='IsOfficial')  # Field name made lowercase.
#    percentage = models.FloatField(db_column='Percentage')  # Field name made lowercase.
#    class Meta:
#        db_table = u'CountryLanguage'
#
#class City(models.Model):
#    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
#    name = models.CharField(max_length=105, db_column='Name')  # Field name made lowercase.
#    countrycode = models.ForeignKey(Country, db_column='CountryCode')  # Field name made lowercase.
#    district = models.CharField(max_length=60, db_column='District')  # Field name made lowercase.
#    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
#    class Meta:
#        db_table = u'City'

