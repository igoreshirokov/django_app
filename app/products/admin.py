from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    model = Category
    extra = 1
    ordering = ['id',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['status', 'name', 'category', 'price']
    search_fields = ['name']
    model = Product
    extra = 1
    ordering = ['id',]

# admin.site.register(Product)
# admin.site.register(Category)