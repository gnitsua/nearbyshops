# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Charity


@admin.register(Charity)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
