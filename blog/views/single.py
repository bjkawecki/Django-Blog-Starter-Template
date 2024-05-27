from django.shortcuts import get_object_or_404, render
from blog.models.post import Post
from blog.models.tag import Tag
from blog.models.source import Source


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, published=True)
    sources = Source.objects.filter(post=post)
    tags = Tag.objects.all()
    related = Post.objects.filter(tag=post.tag).exclude(
        id=post.id).order_by("?")[:3]
    return render(
        request, "single.html", {
            "post": post, "tags": tags, "related": related, "sources": sources}
    )
