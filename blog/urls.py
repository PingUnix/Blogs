from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    #path('blog/<pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    re_path(r'^blogger/(?P<pk>\d+)$', views.blogger_detail_view, name='blogger-detail'),

    #name identifies this particular url mapping, can use this name to reverse the mapper

]
