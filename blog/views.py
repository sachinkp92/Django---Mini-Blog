from django.shortcuts import render
from matplotlib.style import context
from .models import *

# Create your views here.
def show_home(request):
    article_list = Article.objects.all()
    context = {'article_list':article_list}
    return render(request, 'home.html', context)

