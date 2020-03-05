from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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


class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update_form.html"

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("blog:detail", kwargs={"pk": blog_pk})
        return url
