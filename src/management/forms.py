from django import forms
from main.models import Project


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example Site 1'}), label='Project Name')
    project_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}), label='Project Description')
    project_picture = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'custom-file-input'}), label='Project Picture', required=False)
    project_url = forms.URLField(
        required=True, widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.github.com'}), label='Source Code Link')
    author = forms.CharField(
        required=True, label='Project Author', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MyAwesomeUsername'}))
    author_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'contact@me.com'}), label='Author email')
    extra_information = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input'}), label='More Information File', required=False)
    is_in_progess = forms.BooleanField(label='Done', required=False)

    class Meta:
        model = Project
        fields = '__all__'
