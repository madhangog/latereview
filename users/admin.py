# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Audience, Critics

# Register your models here.

admin.site.register(Audience)
admin.site.register(Critics)
