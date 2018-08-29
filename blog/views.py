from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import  User

from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from .models import Comment,Blog, BlogAuthor
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


class BloggerListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'blog.can_access_author'
    #permission_required = 'catalog.can_mark_returned'

    model = BlogAuthor
    paginate_by = 2

    context_object_name = 'my_blogger_list'
    template_name = 'blog/blogger_list.html'


def blogger_detail_view(request, pk):
    try:
        blogger = User.objects.get(pk=pk)

    except User.DoesNotExist:
        raise Http404('Blogger does not exist')

    context = {
        'blogger':blogger,
    }

    return render(request, 'blog/blogger_detail.html', context=context)


class BlogsByAuthorView(generic.ListView):
    model=Blog
    paginate_by = 2
    template_name = 'blog/blog_list_author.html'

    def get_queryset(self):
        ids = self.kwargs['pk']
        author = get_object_or_404(BlogAuthor, pk = ids)
        return Blog.objects.filter(blogger=author)[:5]

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogsByAuthorView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])

        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['contents']

    def get_context_data(self, **kwargs):
        context= super(CommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context

        #return object of blog

    def form_valid(self, form):
        form.instance.commentor = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk':self.kwargs['pk'],})