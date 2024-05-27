from autoslug import AutoSlugField
from django.db import models
from autoslug import AutoSlugField


class Tag(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="name", always_update=True, unique=True)

    def __str__(self):
        return self.name
