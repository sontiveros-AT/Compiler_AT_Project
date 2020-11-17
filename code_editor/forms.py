from django import forms


class FileForm(forms.Form):
    LANGUAGES = (('py', 'Python'), ('java', 'Java'))

    file_name = forms.CharField(max_length=100)
    description = forms.CharField()
    program = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=LANGUAGES)
