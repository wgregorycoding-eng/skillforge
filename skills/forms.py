from django import forms
from django.contrib.auth.forms import PasswordResetForm
from .models import Skill, Resource, StudySession, Category

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email address...'
        })

class SkillForm(forms.ModelForm):

    category = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'list': 'category-options',
            'class': 'form-control',
            'placeholder': 'Select or type a custom category...'
        })
    )

    class Meta:
        model = Skill
        fields = ['category', 'title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_category(self):
        """Automatically get or create the category object from the typed string."""
        category_name = self.cleaned_data.get('category')
        if category_name:
            category_name = category_name.strip()
         
            category_obj, created = Category.objects.get_or_create(name=category_name)
            return category_obj
        return None


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
    class Meta:
        model = StudySession
        fields = ['date', 'duration_minutes', 'reflection_notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
            'reflection_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
        from django.contrib.auth.forms import PasswordResetForm