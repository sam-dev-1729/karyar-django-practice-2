from django.contrib import admin
from .models import Product ,Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    # list_filter = ['name']
    search_fields = ['name']

admin.site.register(Category)
admin.site.register(Product)