from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name="index"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('create/', BlogCreateView.as_view(), name="create"),
]
