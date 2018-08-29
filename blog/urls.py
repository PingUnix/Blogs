from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<pk>', views.BlogsByAuthorView.as_view(), name='blogger-detail'),
    path('blog/<int:pk>/comment', views.CommentCreate.as_view(), name='blog_add_comment'),

]

#path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),
