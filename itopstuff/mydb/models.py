# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Tpi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    business_criticity = models.CharField(max_length=6, blank=True, null=True)
    managementip = models.CharField(max_length=255, blank=True, null=True)
    osfamily_name = models.CharField(max_length=255, blank=True, null=True)
    osfamily_id = models.IntegerField(blank=True, null=True)
    osversion_id = models.IntegerField(blank=True, null=True)
    osversion_name = models.CharField(max_length=255, blank=True, null=True)
    cpu = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    assignedipsinfo = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    projname = models.CharField(max_length=255, blank=True, null=True)
    appinfo = models.TextField(blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'tpi'


    def __str__(self):
        return self.description