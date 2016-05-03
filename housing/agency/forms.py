from django import forms
from .models import Houses

class add_houseForm(forms.ModelForm):
	class Meta:
		model = Houses
		fields = [
			'picture',
			'name', 
			'location', 
			'price',
			'bedrooms',
			'description',
			]
		