from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))

    class Meta:
        model = Post
        fields = ["title", "text", "image", "created_at", "category"]


class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('name', 'text')
