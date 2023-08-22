from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView 

from django.core.paginator import Paginator 
from .models import Post, Category, Author, PostCategory  
from .filters import PostFilter
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

 
class NewsList(ListView):
    model = Post 
    template_name = 'news.html'  
    context_object_name = 'news' 
    ordering = ['-dateCreation'] 
    paginate_by = 10 



class PostDetailView(DetailView):
    template_name = 'news_app/post_detail.html'
    queryset = Post.objects.all()
 
 

class PostCreateView(CreateView):
    template_name = 'news_app/post_create.html'
    form_class = PostForm



class PostUpdateView(UpdateView):
    template_name = 'news_app/post_create.html'
    form_class = PostForm
 
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
 
 

class PostDeleteView(DeleteView):
    template_name = 'news_app/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class PostSearchView(ListView):
    model = Post
    template_name = 'news_app/post_search.html'
    context_object_name = 'news'  
   
    ordering = ['-dateCreation'] 
    
    def get_context_data(self, **kwargs): 
    
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) 
        return context