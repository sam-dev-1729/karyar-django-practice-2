from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Product


@login_required
def product_list(request):
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "shop/product_list.html", context=context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {"product": product}

    return render(request, "shop/product_details.html", context=context)
