from django.shortcuts import render
from .models import Articles

# Create your views here.

def posts_home(request):
    posts = Articles.objects.order_by('-date')

    data = {
        "posts": posts
    }

    return render(request, "posts/home.html", data)


