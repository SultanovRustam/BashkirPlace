from django.shortcuts import get_object_or_404, render

from .models import Product
from .utils import paginator_page


def shop(request):
    page_obj = paginator_page(request, Product.objects.all())
    context = {
        'title': 'Этно-ярмарка',
        'page_obj': page_obj,
    }
    return render(request, 'etnoshop/shop.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product.objects.all(), id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'etnoshop/product_detail.html', context)
