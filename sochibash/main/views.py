from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView

from .models import AdministratorMember
from .utils import paginator_page


class MainView(TemplateView):
    template_name = 'main/index.html'


class AdministrationView(TemplateView):
    template_name = 'main/administration.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'


class ElementsView(TemplateView):
    template_name = 'main/elements.html'


def administration(request):
    page_obj = paginator_page(request, AdministratorMember.objects.all())
    context = {
        'title': 'Администрация',
        'page_obj': page_obj,
    }
    return render(request, 'main/administration.html', context)


def member_detail(request, member_id):
    member = get_object_or_404(AdministratorMember.objects.all(), id=member_id)
    context = {
        'member': member,
    }
    return render(request, 'main/member_detail.html', context)
