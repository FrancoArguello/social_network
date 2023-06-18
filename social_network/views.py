from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from social.forms import PostForm
from social.models import Post, Comment

#LoginRequiredMixin nos sirve para si no esta logueado te redirija a la pagina de login.
class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logged_in_user=request.user
        posts = Post.objects.all()
        form = PostForm()
        
        context={
            'posts': posts,
            'form': form,
            

        }
        return render(request, 'pages/index.html', context)
    
    def post(self, request,*args, **kwargs):
        logged_in_user=request.user
        posts = Post.objects.all()
        form =PostForm(request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = logged_in_user
            new_post.save()
            
        
        context={
            'posts': posts,
            'form':form,
        }
        return render(request, 'pages/index.html', context)