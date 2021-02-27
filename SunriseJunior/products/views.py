from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import *


class CategoryListView(ListView):
    context_object_name = 'categories'
    template_name = 'products/categories.html'
    queryset = Category.objects.all()


class ProductListView(ListView):
    context_object_name = 'products'
    template_name = 'products/product_list.html'

    def get_queryset(self):
        subcategory = self.request.GET.get('subcategory')
        category = self.request.GET.get('category')
        if subcategory:
            return Product.objects.filter(subcategory=subcategory)
        elif category:
            return Product.objects.filter(subcategory__category=category)
        else:
            return Product.objects.all()


class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'products/product_detail.html'
    queryset = Product.objects.all()