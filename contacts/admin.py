from django.contrib import admin
from .models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'telephone', 'category']
    list_display_links = ['id', 'name', 'telephone']
    list_per_page = 10
    search_fields = ['name']


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)