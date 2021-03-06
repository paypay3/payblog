from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, CommentCreateForm, ReplyCreateForm
from .models import Post, Comment, Reply


class BlogListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset


class CategoryView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk)
        return queryset


class TagView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        tag_pk = self.kwargs['pk']
        queryset = Post.objects.order_by('-created_at').filter(tag__pk=tag_pk)
        return queryset


class BlogDetailView(DetailView):
    model = Post


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_create_form.html"
    login_url = '/login'

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        return super().form_invalid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update_form.html"
    login_url = '/login'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("blog:detail", kwargs={"pk": blog_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, "更新されました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")
    login_url = '/login'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)


class BlogLoginView(LoginView):
    template_name = "login.html"


class BlogLogoutView(LogoutView):
    template_name = "logout.html"


class CommentView(CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('blog:detail', pk=post_pk)


class ReplyView(CreateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        comment_pk = self.kwargs['comment_pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
        reply = form.save(commit=False)
        reply.comment = comment
        reply.save()
        return redirect('blog:detail', pk=comment.post.pk)


def api_posts_get(request):
    keyword = request.GET.get('keyword')
    instance_pk = request.GET.get('pk')
    if keyword:
        queryset = Post.objects.filter(title__icontains=keyword)
        if instance_pk:
            queryset = queryset.exclude(pk=instance_pk)
        post_list = [{'pk': post.pk, 'name': str(post)} for post in queryset]
    else:
        post_list = []
    return JsonResponse({'object_list': post_list})
