import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from django.urls import re_path

from config.settings.base import DEBUG


if DEBUG:
    admin_url = "admin/"
else:
    admin_url = os.environ.get("ADMIN_PRODUCTION_URL")


urlpatterns = [
    path(admin_url, admin.site.urls),
    path("", include("blog.urls")),
]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
