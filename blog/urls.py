from django.conf.urls import patterns, include, url
from . import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),

    url(r'^$', views.BlogListView.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)', views.BlogDetailView.as_view(), name="detail"),
    #url(r"^$", blog_list),
)
