from django.shortcuts import render

# Create your views here.
from .models import Comment,Blog

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