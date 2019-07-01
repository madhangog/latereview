# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movies(models.Model):
	movies_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length= 15, unique=True)
	director = models.CharField(max_length=15)
	writer = models.CharField(max_length=15)
	music = models.CharField(max_length=30)
	cast = models.CharField(max_length=50)
	genre = models.CharField(max_length=15)

	def __str__(self):
		return self.name




