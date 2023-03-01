from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm
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
    context = {
        'profile': profile,
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
