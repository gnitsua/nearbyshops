# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models as gismodels
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = gismodels.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
