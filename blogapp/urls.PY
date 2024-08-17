from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns=[
# path('',views.home,name='blog-home'),
  path('about/', views.about,name="blog-about"),
  path('',PostListView.as_view(),name='blog-home'),
  path('post/new',PostCreateView.as_view(template_name="./blog/post_form.html"),name='blog-new'),
  path('post/<int:pk>/', PostDetailView.as_view(template_name="./blog/post_detail.html"), name='blog-detail'),
  path('post/<int:pk>/update', PostUpdateView.as_view(template_name="./blog/post_form.html"), name='blog-update'),
  path('post/<int:pk>/delete', PostDeleteView.as_view(template_name="./blog/post_confirm_delete.html"), name='blog-delete')
]