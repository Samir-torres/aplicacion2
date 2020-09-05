from django.contrib import admin
from .models import Categmate, Bibliografiamate

class Categoriaadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class Bibliografiaadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ("titulo", "categoria", "update")
    search_fields=("titulo", "categoria")


admin.site.register(Categmate, Categoriaadmin)
admin.site.register(Bibliografiamate, Bibliografiaadmin)

# Register your models here.
