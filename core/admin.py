from django.contrib import admin
from .models import Post, Item, Contest


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'slug', 'author', 'image']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'image']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Contest)
class ContextAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
