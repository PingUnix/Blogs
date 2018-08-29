from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import  User

from django.shortcuts import render

# Create your views here.
from .models import Comment,Blog
from django.views import generic

def index(request):

    num_of_blogs = Blog.objects.all().count()
    num_of_comments = Comment.objects.all().count()

    num_of_comments_with_censorship = Comment.objects.filter(status__exact='c').count()
    context={
        'num_of_blogs':num_of_blogs,
        'num_of_comments':num_of_comments,
        'num_of_comments_with_censorship':num_of_comments_with_censorship,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 2

    context_object_name = 'my_blog_list'
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        return Blog.objects.all()[:5]


class BlogDetailView(generic.DetailView):
    model = Blog

'''
def blog_detail_view(request, primary_key):
    try:
        blog = Blog.objects.get(pk=primary_key)

    except Blog.DoesNotExist:
        raise Http404('Blog does not exist')

    context = {
        'blog':blog,
    }

    return render(request, 'blog/blog_detail.html', context=context)
'''


class BloggerListView(generic.ListView):
    model = User
    paginate_by = 2
    context_object_name = 'my_blogger_list'
    template_name = 'blog/blogger_list.html'

    def get_queryset(self):
        return User.objects.all()[:5]


def blogger_detail_view(request, pk):
    try:
        blogger = User.objects.get(pk=pk)

    except User.DoesNotExist:
        raise Http404('Blogger does not exist')

    context = {
        'blogger':blogger,
    }

    return render(request, 'blog/blogger_detail.html', context=context)
