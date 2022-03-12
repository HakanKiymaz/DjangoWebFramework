from django import forms

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name", max_length=250, required=True)
	check = forms.BooleanField(required=False)