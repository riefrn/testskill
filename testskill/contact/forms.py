from django import forms

class contactForm(forms.Form):
	Username = forms.CharField(required=True, max_length=30, help_text='Hanya 30 karakter')
	UserEmail = forms.EmailField(required=True) 
	Message = forms.CharField(required=True, widget=forms.Textarea, )
