from django.shortcuts import render
from .models import Product
# Create your views here.

def products(request):
    all_products = Product.objects.all()
    context = {'all_products' : all_products}
    return render(request, 'products.html', context)