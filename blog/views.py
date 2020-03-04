from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created_at')
