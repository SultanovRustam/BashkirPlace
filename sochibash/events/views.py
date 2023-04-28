from django.shortcuts import render

from .models import Event
from .utils import paginator_page


def index(request):
    page_obj = paginator_page(request, Event.objects.select_related('author'))
    context = {
        'title': 'План мероприятий',
        'page_obj': page_obj,
    }
    return render(request, 'events/index.html', context)

