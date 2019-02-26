from __future__ import unicode_literals

from django.db import models

# Create your models here.
class test_data(models.Model):
	#id = models.IntegerField(primary_key=True)
	#planeID = models.CharField(max_length=256, default='null')
	#RTdata = models.FloatField()
	#SSdata = models.FloatField()
	#TLDdata = models.CharField(max_length=256, default='null')
	#owner = models.CharField(max_length=256, default='null')
	#localMD5 = ""
	#MD5 = models.CharField(max_length=256, default='null')
	id = models.IntegerField(primary_key=True, default='null')
	blocknum = models.IntegerField(max_length=255, default='1')
	data = models.CharField(max_length=1024, default='null')
	MD5 = models.CharField(max_length=256, default='null')

class Plane(models.Model):
	planeID = models.CharField(max_length=255, default='null')
	username = models.CharField(max_length=255, default='null')
	id = models.IntegerField(max_length=11, primary_key=True)

class Metadata(models.Model):
	blockID = models.IntegerField(max_length=11, default='null')
	blockName = models.CharField(max_length=255, default='null')
	parameterUserName = models.CharField(max_length=255, default='null')
	displayOrder = models.IntegerField(max_length=11, default='null')
	id = models.IntegerField(max_length=11, primary_key=True)