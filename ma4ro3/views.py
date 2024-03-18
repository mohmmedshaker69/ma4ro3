from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    obj = Product.objects.all()
    return render(request, 'grid-output.html', {'obj':obj})
