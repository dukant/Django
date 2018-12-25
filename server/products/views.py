from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product
import json


def list_view(request):
    return render(request, 'products\list.html', {
        'products': get_list_or_404(Product)
    })


def detail_view(request, pk):
    return render(request, 'products\detail.html', {
        'object': get_object_or_404(Product, id=pk)})
