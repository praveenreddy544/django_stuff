from django.db import models

# Create your models here.
class Tpi(models.Model):
    id = models.IntegerField(primary_key=True)
    servername = models.CharField(max_length=255, blank=True, null=True)
    fqdn = models.CharField(max_length=255, blank=True, null=True)
    patchversion = models.CharField(max_length=255, blank=True, null=True)
    osversion = models.CharField(max_length=255, blank=True, null=True)
    updatesavailablecount = models.CharField(max_length=255, blank=True, null=True)
    updateslist = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'patch_newinfo'


    def __str__(self):
        return self.servername