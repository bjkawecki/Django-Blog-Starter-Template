from django_resized import ResizedImageField
from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from .image import Image
from .tag import Tag


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    teaser = models.TextField(max_length=500, blank=True)
    slug = AutoSlugField(populate_from="title",
                         always_update=True, unique=True)
    text = models.TextField()
    published = models.BooleanField(default=False)
    image = ResizedImageField(upload_to="images/%Y/%m/%d", blank=True)
    tag = models.ForeignKey(
        Tag, on_delete=models.DO_NOTHING, related_name="tag")

    def get_absolute_url(self):
        return reverse("post_single", args=[self.slug])

    class Meta:
        ordering = ["-created_at"]
        app_label = "blog"

    def __str__(self):
        return self.title
