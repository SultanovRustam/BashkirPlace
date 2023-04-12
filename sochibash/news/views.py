from django.shortcuts import get_object_or_404, render

from .models import News, User
from .utils import paginator_page


def profile(request, username):
    author = get_object_or_404(User, username=username)
    page_obj = paginator_page(request, author.news.select_related("author"))
    context = {"author": author, "page_obj": page_obj}
    return render(request, "news/profile.html", context)


def index(request):
    page_obj = paginator_page(request, News.objects.select_related('author'))
    context = {
        'title': 'Последние новости на сайте',
        'page_obj': page_obj,
    }
    return render(request, 'news/index.html', context)


def news_detail(request, news_id):
    news = get_object_or_404(News.objects.select_related('author'), id=news_id)
    context = {
        'news': news,
    }
    return render(request, 'news/news_detail.html', context)
