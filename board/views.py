from django.shortcuts import render

from .models import Post
# Create your views here.
def main_page(request):
    posts = Post.objects.all()
    
    context = {
        "posts": posts
    }
    
    return render(request, "board/board_main.html", context)