from django.views.generic.base import TemplateView
from django.shortcuts import render
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


class GenericView(TemplateView):
    template_name = 'main/generic.html'


def administration(request):
    page_obj = paginator_page(request, AdministratorMember.objects.all())
    context = {
        'title': 'Администрация',
        'page_obj': page_obj,
    }
    return render(request, 'main/administration.html', context)
