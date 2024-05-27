from django.contrib import admin

from .models.image import Image
from .models.post import Post
from .models.source import Source
from .models.tag import Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ("title", "subtitle", "teaser", "text", "published", "created_at", "image", "tag")
    list_display = ("title", "slug", "created_at")


admin.site.register([Source, Tag])
