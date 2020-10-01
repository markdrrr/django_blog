# Register your models here.
from django.contrib import admin

from .models import Product, Image
# admin.site.register(Product)
# admin.site.register(Image)

class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    inlines = [ProductImageInline]

    class Meta:
         model = Product

admin.site.register(Product, ProductAdmin )