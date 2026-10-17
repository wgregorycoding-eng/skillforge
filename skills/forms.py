from django import forms
from .models import Skill, Resource, StudySession

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={
                'class': 'form-control', 
                'list': 'category-options', 
                'placeholder': 'Select or type a category...'
            }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'url', 'resource_type', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'resource_type': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class StudySessionForm(forms.ModelForm):
    class Meta
    