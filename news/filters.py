from django_filters import FilterSet 
from .models import Post, Category
 
 

class PostFilter(FilterSet):
   
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'], 
            'dateCreation': ['gt'], 
            'text': ['icontains'], 
            'author': ['exact'],
        }
