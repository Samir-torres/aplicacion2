from django.contrib import admin
from .models import Categinfor, Bibliografiainfor

class Categoriaadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class Bibliografiaadmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ("titulo", "categoria", "update")
    search_fields=("titulo", "categoria")


admin.site.register(Categinfor, Categoriaadmin)
admin.site.register(Bibliografiainfor, Bibliografiaadmin)
# Register your models here.
