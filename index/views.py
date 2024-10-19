from django.shortcuts import render
from .models import NewsCategory, News


# Create your views here.
def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {
        'news': news,
        'categories': categories
    }

    return render(request, 'home.html', context)



def news_category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    exact_news = News.objects.filter(news_category=category)
    context = {'category': category, 'news': exact_news}
    return render(request, 'category.html', context)


def news_page(request, pk):
    news = News.objects.get(id=pk)
    context = {'news': news}
    return render(request, 'news.html', context)