from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid
from django.urls import reverse


class Blog(models.Model):
    #no primary key is declared, Model blog will ge id for the pk automatically

    title = models.CharField(max_length=300)
    contents = models.CharField(max_length=65535)
    publish_date = models.DateField(null=True, blank=True,default=date.today())
    blogger = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(),help_text='id for comment')
    contents = models.CharField(max_length=1000)
    comment_date = models.DateField(null=True, blank=True, default=date.today())
    commentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True, blank=False)

    COMMENT_STATUS= (
        ('c', 'censorship'),
        ('p', 'published'),
    )
    status = models.CharField(
        max_length=1,
        choices=COMMENT_STATUS,
        blank=True,
        default='c',
        help_text='status of comment'
    )

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return f'{self.blog.title} ({self.commentor})'


class BlogAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=516, help_text='innput the detail here')

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.user.username