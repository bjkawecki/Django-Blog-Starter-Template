from django.views.generic import ListView
from blog.models.post import Post
from blog.models.tag import Tag


class TagListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            tag__slug__in=[self.kwargs["tag"]])
        tag = self.kwargs["tag"]
        context["topic"] = tag
        context["posts"] = Post.objects.filter(tag__slug=tag)
        context["tags"] = Tag.objects.order_by('name')
        return context

    def get_template_names(self):
        return "posts_by_tag.html"
