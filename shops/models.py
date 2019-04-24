# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models as gismodels
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = gismodels.PointField()
    address = models.CharField(max_length=400)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Shop, on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.Charfield(max_length=100)
    menu_item = models.ManyToManyField(MenuItem)
