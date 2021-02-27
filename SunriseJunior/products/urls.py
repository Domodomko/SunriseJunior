from django.urls import path
from .views import *


urlpatterns = [
    path('categories', CategoryListView.as_view(), name='categories'),
    path('products', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products'),
]