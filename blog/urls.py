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
    CommentView,
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
    path('comment/<int:post_pk>/', CommentView.as_view(), name='comment'),
]
