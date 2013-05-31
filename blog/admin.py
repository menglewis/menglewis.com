from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	fields = ['published', 'title', 'slug', 'author', 'content']
	list_display = ['published', 'title', 'updated_at']
	list_display_links = ['title']
	list_editable = ['published']
	list_filter = ['published', 'updated_at']
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
