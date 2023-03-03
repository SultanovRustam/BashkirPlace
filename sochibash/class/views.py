from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Class, User


@staff_member_required
def class_create(request):
    context = {
        'title': 'Новое занятие'
    }
