from django.contrib import admin
from .models import Categelectro, Bibliografiaelectro

class Categoriaadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class Bibliografiaadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ("titulo", "categoria", "update")
    search_fields=("titulo", "categoria")


admin.site.register(Categelectro, Categoriaadmin)
admin.site.register(Bibliografiaelectro, Bibliografiaadmin)


# Register your models here.
