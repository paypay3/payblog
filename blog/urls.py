from django.urls import path

from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogLoginView,
    BlogLogoutView,
    CategoryView,
    TagView,
    CommentView,
    ReplyView,
    api_posts_get,
)

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name="index"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('login/', BlogLoginView.as_view(), name="login"),
    path('logout/', BlogLogoutView.as_view(), name="logout"),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('tag/<int:pk>/', TagView.as_view(), name='tag'),
    path('comment/<int:post_pk>/', CommentView.as_view(), name='comment'),
    path('reply/<int:comment_pk>/', ReplyView.as_view(), name='reply'),
    path('api/posts/get/', api_posts_get, name='api_posts_get'),
]
