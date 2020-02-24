from django import forms
from .models import Think

from django.core.exceptions import ValidationError



class ThinkForm(forms.ModelForm):
    class Meta:
        model=Think
        fields=['title','slug','body','opis']
        
        widgets={
            'title': forms.TextInput (attrs={'class': 'form-control'}),
            'slug': forms.TextInput (attrs={'class': 'form-control'}),
            'body': forms.Textarea (attrs={'class': 'form-control'}),
            'opis': forms.Textarea (attrs={'class': 'form-control'}),
            
            }
        def clean_slug(self):
            new_slug=self.cleaned_data['slug'].lower()
            if new_slug=='create':
             raise ValidationError('Slug may not be "Create"')
            return new_slug