from django.urls import path

from .views.home import HomeView
from .views.single import post_single
from .views.about import about
from .views.impressum import impressum
from .views.services import services
from .views.tag_list import TagListView

urlpatterns = [
    path("posts/<slug:post>/", post_single, name="post_single"),
    path("about/", about, name="about"),
    path("", HomeView.as_view(), name="homepage"),
    path("impressum/", impressum, name="impressum"),
    path("services/", services, name="services"),
    path("tags/<slug:tag>/", TagListView.as_view(), name="TagListView"),
]
