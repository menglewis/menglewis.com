from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'
	fields = ['published', 'title', 'slug', 'author', 'content']
	list_display = ['published', 'title', 'updated']
	list_display_links = ['title']
	list_editable = ['published']
	list_filter = ['published', 'updated']
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)