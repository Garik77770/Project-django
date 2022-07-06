from django.shortcuts import render

from blog.models import Post

posts = [
    {
        'author': 'max',
        "title": "blog post 1",
        "content": "first post content",
        "date_posted": 'Feb 25, 2022',
    },
    {
        "author": "Ian",
        "title": "blog post 2",
        "content": "Second post content",
        "date_posted": "Feb 23, 2022",
    },
]


def home(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)


def about(request):
    context = {
        'title': 'about page'
    }
    return render(request, 'blog/about.html', context)
# Create your views here.
