from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClassForm
from .models import Class
from .utils import paginator_page


def index(request):
    page_obj = paginator_page(request, Class.objects.select_related('author'))
    context = {
        'title': 'Занятия',
        'page_obj': page_obj,
    }
    return render(request, 'class/index.html', context)


@staff_member_required
def class_create(request):
    context = {
        'title': 'Новое занятие'
    }
    form = ClassForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        new_class = form.save(commit=False)
        new_class.author = request.user
        new_class.save()
        return redirect('class:index')
    context['form'] = form
    return render(request, 'class/class_create.html', context)


@staff_member_required
def class_edit(request, class_id):
    class_alt = get_object_or_404(Class, id=class_id)
    if request.user != class_alt.author:
        return redirect('class:index')
    context = {
        'title': 'Редактировать занятие',
        'class': class_alt,
        'is_edit': True
    }
    form = ClassForm(request.POST or None, files=request.FILES or None,
                     instance=class_alt)
    if form.is_valid():
        form.save()
        return redirect("class:index", class_alt.id)
    context["form"] = form
    return render(request, "class/class_create.html", context)
