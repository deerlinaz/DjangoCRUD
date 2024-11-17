# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Discover(models.Model):
    cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='cname', primary_key=True)  # The composite primary key (cname, disease_code) found, that is not supported. The first column is selected.
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    did = models.ForeignKey('Diseasetype', models.DO_NOTHING, db_column='did', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class Diseasetype(models.Model):
    did = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseasetype'


class Doctor(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    ddegree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Patientdisease(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patientdisease'


class Patients(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'patients'


class Publicservant(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicservant'


class Record(models.Model):
    email = models.OneToOneField(Publicservant, models.DO_NOTHING, db_column='email', primary_key=True)  # The composite primary key (email, cname, disease_code) found, that is not supported. The first column is selected.
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)


class Specialize(models.Model):
    sid = models.OneToOneField(Diseasetype, models.DO_NOTHING, db_column='sid', primary_key=True)  # The composite primary key (sid, email) found, that is not supported. The first column is selected.
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'specialize'
        unique_together = (('sid', 'email'),)


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    uname = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
