from django import forms


class FileForm(forms.Form):
    LANGUAGES = (('python', 'Python'), ('java', 'Java'))

    program = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=LANGUAGES, widget=forms.Select(attrs={'class': 'form-control'}))


class ProjectForm(forms.Form):
    LANGUAGES = (('python', 'Python'), ('java', 'Java'))

    project_name = forms.CharField(max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': "Enter project name"}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Project Description"}))
    language = forms.ChoiceField(choices=LANGUAGES, widget=forms.Select(attrs={'class': 'form-control'}))
