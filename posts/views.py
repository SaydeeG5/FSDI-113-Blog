from django.views.generic import (
    CreateView, 
    DetailView,
    UpdateView, 
    DeleteView, 
    ListView
)

from .models import Post 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post 

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post 

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body", "active"]

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post 
    fields = ["title", "subtitle", "body", "active"]

class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post 
    success_url = reverse_lazy("list")

