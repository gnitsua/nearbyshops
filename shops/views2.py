# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.measure import Distance
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from shops.forms import BuildingNameForm
from shops.forms import LatLngForm
from shops.models import Shop
import json


def shops(request):
    if request.method == "POST":
        form = LatLngForm(request.POST)
        if (form.is_valid()):
            pass
            # data = Shop.objects.filter(location__distance_lt=(form.cleaned_data["point"], Distance(m=5000)))
            # return HttpResponse(serialize('geojson', data, geometry_field='location', fields=('name',)),
            #                     content_type="application/json")
        else:
            print(form.errors)
            return HttpResponseBadRequest(str(form.errors))
    else:
        form = LatLngForm()
        return render(request, 'latlngform.html', {'form': form})


@require_http_methods(["GET", "POST"])
def buildings(request):
    if request.method == "POST":
        form = BuildingNameForm(request.POST)

        if (form.is_valid()):
            print(form.cleaned_data)
            # data = Shop.objects.filter(name=form.cleaned_data["name"])
            building = form.cleaned_data["building"]
            return render(request, 'map.html', {'buildings': [building]})
    else:
        form = BuildingNameForm()
        return render(request, 'buildingnameform.html', {'form': form})
