from django.contrib import admin
from .models import Category, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'telephone', 'category', 'showfild']
    list_display_links = ['id', 'name']
    list_per_page = 10
    search_fields = ['name']
    list_editable = ['telephone', 'showfild']

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)