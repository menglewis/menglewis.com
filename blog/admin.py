from django.contrib import admin
from .models import Post, Comment

class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ['published', 'title', 'slug', 'author', 'content']
    list_display = ['published', 'title', 'updated_at']
    list_display_links = ['title']
    list_editable = ['published']
    list_filter = ['published', 'updated_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentsInline]

class CommentAdmin(admin.ModelAdmin):
    fields = ['content']
    list_display = ['post', 'content', 'updated_at']
    list_display_links = ['post']
    list_filter = ['updated_at']
    search_fields = ['post', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
