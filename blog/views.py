from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-created_at')
