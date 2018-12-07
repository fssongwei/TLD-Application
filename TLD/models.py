from __future__ import unicode_literals

from django.db import models

# Create your models here.
class data(models.Model):
	id = models.IntegerField(primary_key=True)
	planeID = models.CharField(max_length=256, default='null')
	RTdata = models.FloatField()
	SSdata = models.FloatField()
	TLDdata = models.CharField(max_length=256, default='null')
	owner = models.CharField(max_length=256, default='null')
	localMD5 = ""
	MD5 = models.CharField(max_length=256, default='null')