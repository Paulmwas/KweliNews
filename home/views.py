from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all()

    return render(request, 'home.html', {'articles':articles})