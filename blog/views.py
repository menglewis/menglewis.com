# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView


class PublishedPostsMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostsMixin, self).get_queryset()
        return queryset.filter(published=True)

class BlogListView(PublishedPostsMixin, ListView):
	model = Post
	template_name = "post_list.html"


class BlogDetailView(PublishedPostsMixin, DetailView):
	model = Post
	template_name = "post_detail.html"
