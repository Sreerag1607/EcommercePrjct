from django.contrib import admin
from .models import Category,Product

# Register your models here.
# this class is created to see the tables in a good manner in admin panel instead of previous admin panel we used
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)