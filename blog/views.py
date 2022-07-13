from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = '-date_posted'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/blog/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    context = {
        'title': 'about page'
    }
    return render(request, 'blog/about.html', context)
# Create your views here.
