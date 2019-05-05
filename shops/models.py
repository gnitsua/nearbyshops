# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models as gismodels
from django.db import models

class Charity(models.Model):
    name = models.CharField(max_length=100)
    ein = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    location = gismodels.PointField()