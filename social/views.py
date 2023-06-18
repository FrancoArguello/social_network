from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import View
from requests import request
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls.base import reverse_lazy




class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body']
    template_name = 'pages/posts/edit.html'
    success_url = reverse_lazy('home')

    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    fields = ['body']
    template_name = 'pages/posts/delete.html'
    success_url = reverse_lazy('home')

    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
