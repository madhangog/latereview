# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone



# Create your models here.

class Audience(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=30)
	mobile = models.CharField(max_length=12)
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=False)
		
	def __str__(self):
		return self.username