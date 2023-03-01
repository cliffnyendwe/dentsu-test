# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Count(models.Model):
    service_names = models.CharField(max_length=80, unique=True)
    statue_code = models.CharField(max_length=30, unique=True)
    start_date = models.DateField(unique=True)
    end_date = models.DateField(unique=True)
    
