from django.shortcuts import render

from .models import Product
from .utils import paginator_page


def shop(request):
    page_obj = paginator_page(request, Product.objects.all())
    context = {
        'title': 'Этно-ярмарка',
        'page_obj': page_obj,
    }
    return render(request, 'etnoshop/shop.html', context)
