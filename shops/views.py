# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core import serializers
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from shops.forms import ShopForm
from shops.forms import ShopSearchForm
from shops.models import Charity


@csrf_exempt
@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, 'index.html')


@csrf_exempt
@require_http_methods(["GET", "POST"])
def shops(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/shops/')
    else:
        results = Charity.objects.all()
        results = json.loads(serializers.serialize('geojson', results))
        if ("application/json" in request.META.get('HTTP_ACCEPT')):
            return JsonResponse({"data": results})
        else:
            return render(request, 'map.html', {"shops": json.dumps(results)})




@csrf_exempt
@require_http_methods(["GET"])
def shops_create_form(request):
    form = ShopForm()
    return render(request, 'shopcreate.html', {'form': form})


@csrf_exempt
@require_http_methods(["GET", "POST"])
def shops_search(request):
    if request.method == "POST":
        form = ShopSearchForm(request.POST)
        if (form.is_valid()):
            #if it's an empty form we return everything
            results = Charity.objects.all()
            if(form.cleaned_data["text"] != None and form.cleaned_data["text"] != ""):
                #if the user gave us a text string, pick everything that is close
                # let's make names more important than descriptions
                vector = SearchVector('name', weight='A') + SearchVector('description', weight='B')
                query = SearchQuery(form.cleaned_data["text"])
                results = results.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.1).order_by('-rank')
            if(form.cleaned_data["lat"] != None and form.cleaned_data["lng"] != None):
                #if the user gave us a location let's sort by location
                location = Point(x=form.cleaned_data["lat"],y=form.cleaned_data["lng"],srid=4326)
                results = results.annotate(distance=Distance("location", location)).order_by("distance")
            #convert to a json friendly pyhton object
            results = json.loads(serializers.serialize('geojson',results))
            if ("application/json" in request.META.get('HTTP_ACCEPT')):
                return JsonResponse({"data":results})
            else:
                print(results)
                return render(request,'map.html',{"shops":json.dumps(results)})
        else:
            return HttpResponseBadRequest(str(form.errors))
    else:
        form = ShopSearchForm()
        return render(request, 'shopsearch.html', {'form': form})
