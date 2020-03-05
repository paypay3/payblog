from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import Post


class BlogListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class BlogDetailView(DetailView):
    model = Post


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_create_form.html"
