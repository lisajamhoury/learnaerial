from django import forms

class NewsletterForm(forms.Form):
	fname = forms.CharField(max_length=50, required=False)
	lname = forms.CharField(max_length=50, required=False)
	email = forms.EmailField()
