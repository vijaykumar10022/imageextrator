from django.forms import ModelForm

from myapp.models import Mymodel

class Myform(ModelForm):
	class Meta:
		model=Mymodel
		fields='__all__'
