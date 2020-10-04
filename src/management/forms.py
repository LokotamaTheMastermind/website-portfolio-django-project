from django import forms
from main.models import Project


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Project Name')
    project_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}), label='Project Description')
    project_picture = forms.ImageField(
        label='Project Picture', allow_empty_file=True)
    project_picture = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    project_url = forms.URLField(
        required=True, widget=forms.URLInput(attrs={'class': 'form-control'}), label='Source Code Link')
    author = forms.CharField(
        required=True, label='Project Author', widget=forms.TextInput(attrs={'class': 'form-control'}))
    author_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}), label='Author email')

    class Meta:
        model = Project
        fields = '__all__'
