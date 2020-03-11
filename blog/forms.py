from django import forms
from django.urls import reverse_lazy

from .models import Post, Comment, Reply
from .widgets import SuggestWidget


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))

    class Meta:
        model = Post
        fields = ["title", "text", "image", "created_at", "category", "tag", "relation_posts"]
        widgets = {
            'relation_posts': SuggestWidget(attrs={'data-url': reverse_lazy('blog:api_posts_get')}),
        }


class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('name', 'text')


class ReplyCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Reply
        fields = ('name', 'text')
