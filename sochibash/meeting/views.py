from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, ProfileForm
from .models import Profile
from .utils import paginator_page


def index(request):
    page_obj = paginator_page(request,
                              Profile.objects.select_related('author'))
    context = {
        'title': 'Профили пользователей',
        'page_obj': page_obj,
    }
    return render(request, 'meeting/index.html', context)


def profile(request, username):
    profile = get_object_or_404(Profile.objects.select_related('author'),
                                author=username)
    context = {
        'profile': profile,
    }
    return render(request, 'meeting/profile_detail.html', context)


def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile.objects.select_related('author'),
                                id=profile_id)
    comments = profile.comments.all().select_related("author")
    context = {
        'profile': profile,
        "form": CommentForm(),
        "comments": comments,
    }
    return render(request, 'meeting/profile_detail.html', context)


@login_required
def profile_create(request):
    context = {
        'title': 'Создать профиль'
    }
    form = ProfileForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        new_profile = form.save(commit=False)
        new_profile.author = request.user
        new_profile.save()
        return redirect('meeting:profile', request.user)
    context['form'] = form
    return render(request, 'meeting/create_profile.html', context)


@login_required
def profile_edit(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.user != profile.author:
        return redirect('meeting:profile_detail', profile_id)
    context = {
        'title': 'Редактировать профиль',
        'profile': profile,
        'is_edit': True
    }
    form = ProfileForm(request.POST or None, files=request.FILES or None,
                       instance=profile)
    if form.is_valid():
        form.save()
        return redirect("meeting:profile_detail", profile.id)
    context["form"] = form
    return render(request, "meeting/create_profile.html", context)


@login_required
def profile_delete(request):
    if request.method == 'POST':
        profile = Profile.objects.get(author=request.user)
        profile.delete()
        return redirect('meeting:index')
    return render(request, 'meeting/profile_delete.html')


@login_required
def add_comment(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.profile = profile
        form.save()
    return redirect('meeting:profile_detail', profile_id=profile_id)
