from django.shortcuts import render
from .models import Products

# Create your views here.

def all_products(request):
    """ A view to show all products, sorting and search """

    products = Products.objects.all()

    context = {
        'products': products, 
    }

    return render(request, 'products/products.html', context)