from django import forms
#this class is to perform the post request
from .models import RestaurantLocation
from .validators import validate_category, validate_email

class RestaurantCreateForm(forms.Form):
	name 			= forms.CharField()
	location 		= forms.CharField(required=False)
	category 		= forms.CharField(required=False)
	
	def clean_name(self): #called when we do forms.is_valid in the restaurant_createview method
		name = self.cleaned_data.get("name")
		if name == "hello":
			raise forms.ValidationError("not a vaid name")
		return name	

class RestaurantLocationCreateForm(forms.ModelForm):
	#email = forms.EmailField(required= False, validators=[validate_email])
	category = forms.CharField(required = False, validators=[validate_category])
	class Meta:
		model = RestaurantLocation
		fields = [
			'name',
			'location',
			'category',
		]
		
	def clean_name(self): #called when we do forms.is_valid in the restaurant_createview method
		name = self.cleaned_data.get("name")
		if name == "hello":
			raise forms.ValidationError("not a vaid name")
		return name	

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	if "edu" in email:
	# 		raise forms.ValidationError("we do not accepts edu emails")
	# 	return email	
