from django.contrib import admin
from .models import Type,Flower

admin.site.register(Type)


class AdminView(admin.ModelAdmin):
    list_display = ('pk','title' , 'category' , 'publication_date')
    list_display_links = ('pk','title')
    list_per_page = 10

admin.site.register(Flower , AdminView)