from django.db import models
from .post import Post


class Source(models.Model):
    name = models.CharField(max_length=250)
    hyperlink = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             blank=True, null=True)

    def __str__(self):
        return self.name
