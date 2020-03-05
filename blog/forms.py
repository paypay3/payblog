from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))

    class Meta:
        model = Post
        fields = ["title", "text", "image", "created_at", "category"]
