from django.contrib.gis import forms

class LatLngForm(forms.Form):
    point = forms.PointField(widget=forms.OSMWidget(attrs={'default_lon': -75.1899,
           'default_lat': 39.9566}))

class BuildingNameForm(forms.Form):
	CHOICES = ()# start out with no defaults
	name = forms.CharField(widget=forms.Select(choices=CHOICES))
	def __init__(self, *args,**kwargs):
		self.CHOICES = kwargs.pop('names')
        super(BuildingNameForm, self).__init__(*args, **kwargs)


