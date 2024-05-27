from django.views.generic import ListView
from blog.models.post import Post
from blog.models.tag import Tag


class HomeView(ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.order_by("-created_at")[3:].all()
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            latest_post = Post.objects.order_by("-created_at")[:1].get()
        except Post.DoesNotExist:
            latest_post = None
        context["latest_post"] = latest_post
        context["posts_image"] = Post.objects.order_by(
            "-created_at")[1:3].all()
        # context.update(posts=Post.objects.order_by("-created_at")[3:])
        context["tags"] = Tag.objects.all()
        return context

    def get_template_names(self):
        if self.request.htmx:
            return "components/post-list.html"
        return "list.html"
