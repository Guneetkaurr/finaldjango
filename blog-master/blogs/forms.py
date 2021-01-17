from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title : ','text': 'Text : '}
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of your blog'}),
            'text': forms.Textarea(attrs={'cols': 100, 'placeholder': 'Blog text...'})
        }