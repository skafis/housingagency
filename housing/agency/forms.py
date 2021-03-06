from django import forms
from .models import Houses, Contact

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
		
class contactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			'name',
			'email',
			'message',
		]