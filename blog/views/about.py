from django.shortcuts import render
from blog.models.tag import Tag


def about(request):
    tags = Tag.objects.all()
    return render(
        request,
        "about.html",
        {
            "tags": tags,
        },
    )
