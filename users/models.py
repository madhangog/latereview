# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from polymorphic.models import PolymorphicModel



# Create your models here.


class reviewer(PolymorphicModel):
	reviewer_id = models.AutoField(primary_key=True)
	
class Audience(reviewer):
	# user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=300)
	mobile = models.CharField(max_length=12)
	date_joined = models.DateTimeField(default=timezone.now)
		
	def __str__(self):
		return self.username



class Critics(reviewer):
	# critic_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=30)
	mobile = models.CharField(max_length=12)
	email = models.EmailField(max_length=50)
	date_joined = models.DateTimeField(default=timezone.now)
		
	def __str__(self):
		return self.name