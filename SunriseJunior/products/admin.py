from django.contrib import admin
from .models import *


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    search_fields = ()
    fieldsets = (
        (None, {
            "fields": (
                'name',
            ),
        }),
    )
    inlines = [SubCategoryInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    search_fields = ()
    fieldsets = (
        (None, {
            "fields": (
                'name',
                'description',
                'subcategory'
            ),
        }),
    )
