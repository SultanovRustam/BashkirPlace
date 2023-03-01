from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewsForm
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


@staff_member_required
def news_create(request):
    context = {
        'title': 'Новая новость'
    }
    form = NewsForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        new_news = form.save(commit=False)
        new_news.author = request.user
        new_news.save()
        return redirect('news:profile', request.user)
    context['form'] = form
    return render(request, 'news/create_news.html', context)


@staff_member_required
def news_edit(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.user != news.author:
        return redirect('news:news_detail', news_id)
    context = {
        'title': 'Редактировать запись',
        'news': news,
        'is_edit': True
    }
    form = NewsForm(request.POST or None, files=request.FILES or None,
                    instance=news)
    if form.is_valid():
        form.save()
        return redirect("news:news_detail", news.id)
    context["form"] = form
    return render(request, "news/create_news.html", context)
