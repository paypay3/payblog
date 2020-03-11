from django.contrib import admin
from .forms import PostForm
from .models import Post, Category, Tag, Comment, Reply


class PostAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
