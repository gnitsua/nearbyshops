from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget

from shops.models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'description', 'location')
        widgets = {'location': LeafletWidget()}


class LatLngForm(forms.Form):
    point = forms.PointField(widget=forms.OSMWidget(attrs={'default_lon': -75.1899,
                                                           'default_lat': 39.9566}))


class shopChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name


class ShopSearchForm(forms.Form):
    text = forms.CharField(required=False)
    lat = forms.FloatField(required=False)
    lng = forms.FloatField(required=False)
