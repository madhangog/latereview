# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Audience(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=30)
	mobile = models.CharField(max_length=12)
	
	def __str__(self):
		return self.username