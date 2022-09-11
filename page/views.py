from django.shortcuts import render
from .models import Page

# Create your views here.

def other (request):
    pages = Page.objects.all()
    return render(request, 'page/other.html', {'pages': pages})
