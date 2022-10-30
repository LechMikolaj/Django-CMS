from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
    posts_list=Post.objects.order_by('pub_date')[:5]
    context={
        'posts_list': posts_list,
    }
    return render(request,'index.html' , context)

