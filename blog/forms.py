from django import forms
from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'user', 'body_text', 'created_at')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'user': forms.Select(attrs={'class': 'form-control'}),
        'body_text': forms.Textarea(attrs={'class': 'form-control'}),
        'created_at': forms.TextInput(attrs={'class': 'form-control'}),
        'updated_at': forms.TextInput(attrs={'class': 'form-control'}),

    }
