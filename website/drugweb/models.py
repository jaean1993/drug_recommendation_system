# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cure(models.Model):
    cure_id = models.AutoField(db_column='CURE_ID', primary_key=True)  # Field name made lowercase.
    drug_name = models.CharField(db_column='DRUG_NAME', max_length=255)  # Field name made lowercase.
    illness_name = models.CharField(db_column='ILLNESS_NAME', max_length=255)  # Field name made lowercase.
    rating = models.IntegerField(db_column='RATING', blank=True, null=True)  # Field name made lowercase.
    alcohol = models.CharField(db_column='ALCOHOL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rx_otc = models.CharField(db_column='RX_OTC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    popularity = models.FloatField(blank=True, null=True)
    csa = models.CharField(db_column='CSA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pregnancy = models.CharField(max_length=100, blank=True, null=True)
    review_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CURE'


class Drugdetails(models.Model):
    drug_id = models.AutoField(db_column='DRUG_ID', primary_key=True)  # Field name made lowercase.
    drug_name = models.CharField(db_column='DRUG_NAME', max_length=255)  # Field name made lowercase.
    drug_details = models.TextField(db_column='DRUG_DETAILS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DRUGDETAILS'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
