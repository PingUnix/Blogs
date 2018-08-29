from django.contrib import admin
from .models import Blog, Comment, BlogAuthor, VIP

# Register your models here.
#admin.site.register(Blog)
#admin.site.register(Comments)


class CommentInline(admin.TabularInline):
    model = Comment

# Register the Admin classes for BookInstance using the decorator
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'blog',
        'contents',
        'comment_date',
        'commentor',
        'status'
    )
    fieldsets = (
        (None, {
            'fields': ('id', 'blog', 'contents')
        }),
        ('Availability', {
            'fields': ('comment_date', 'commentor')
        }),
    )
admin.site.register(Comment, CommentAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'contents',
        'publish_date',
        'blogger',
    )
    fieldsets = (
        (None, {
            'fields': ('title', 'contents')
        }),
        ('Availability', {
            'fields': ('publish_date', 'blogger')
        }),
    )
    inlines = [CommentInline]

admin.site.register(Blog, BlogAdmin)

class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bio',
    )
admin.site.register(BlogAuthor, BlogAuthorAdmin)


class VIPAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'join_date',
    )
admin.site.register(VIP, VIPAdmin)