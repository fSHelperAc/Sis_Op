from django import forms

from .models import Comment
from django.forms.widgets import HiddenInput

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body', 'comment_parent')
        #fields = ('author', 'body')
        widgets = {'comment_parent': forms.HiddenInput()}