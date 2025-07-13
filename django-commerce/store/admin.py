# admin.py
from django.contrib import admin
from .models import Category, Product, Customer, Cart, CartItem, Order, ProductColor, ProductSize, OrderItem


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 1





class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductColorInline, ProductSizeInline]