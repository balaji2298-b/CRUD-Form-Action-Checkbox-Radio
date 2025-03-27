from django import forms
from myapp.models import Checkbox

class CheckboxForm(forms.ModelForm):
	class Meta:
		model = Checkbox
		fields = ['name','language','gender']
		
  
