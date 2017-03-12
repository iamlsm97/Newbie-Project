from django.forms import ModelForm
from basic.models import Cafe

class CafeForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'time', 'locLat', 'locLng', 'Roastery', 'Engname']

