from django import forms


class HelloWorldForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()