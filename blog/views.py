from django.shortcuts import render
from .models import Post

# Create your views here.
def blog (request):
    post = Post.objects.all()
    return render(request, 'blog/blog.html', {'post': post})