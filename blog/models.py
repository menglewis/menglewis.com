from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    author = models.ForeignKey(User, related_name='posts')
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __save__(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("blog:detail", (), {"slug": self.slug})

    class Meta:
        ordering = ["-created_at", "title"]

class Comment(TimeStampedModel):
    content = models.TextField()
    author = models.ForeignKey(User, related_name='comments')
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.content[0:20]

    class Meta:
        ordering = ["created_at"]
