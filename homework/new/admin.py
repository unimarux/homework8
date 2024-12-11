from django.contrib import admin
from .models import Category,Book

admin.site.register(Category)


class AdminView(admin.ModelAdmin):
    list_display = ('pk','title' , 'category' , 'publication_date' , 'genre')
    list_display_links = ('pk','title')
    list_per_page = 10

admin.site.register(Book , AdminView)