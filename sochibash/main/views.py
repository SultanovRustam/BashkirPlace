from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView

from .models import AdministratorMember, Banner
from .utils import paginator_page


def main_view(request):
    try:
        banner = Banner.objects.get(published=True)
    except Banner.DoesNotExist:
        banner = None
    return render(request, 'main/index.html', {'banner': banner})


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
