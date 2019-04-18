from django.contrib.gis import forms
from shops.models import Shop

class LatLngForm(forms.Form):
    point = forms.PointField(widget=forms.OSMWidget(attrs={'default_lon': -75.1899,
                                                           'default_lat': 39.9566}))



class BuildingChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name

class BuildingNameForm(forms.Form):
    building = BuildingChoiceField(queryset=Shop.objects.all(), to_field_name="name", empty_label=None)