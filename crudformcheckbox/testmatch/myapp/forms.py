from django import forms
from myapp.models import Checkbox

class CheckboxForm(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	language=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	gender=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Checkbox
		fields = ['name','language','gender']
		
  
