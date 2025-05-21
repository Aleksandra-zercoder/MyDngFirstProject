from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    qs = News.objects.select_related('author').all()
    return render(request, 'news/news_list.html', {'news_list': qs})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})
from django.shortcuts import render

# Create your views here.
