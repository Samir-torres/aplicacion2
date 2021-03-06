from django.db import models

class Categmate(models.Model):
    nombre = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__ (self):
        return self.nombre


class Bibliografiamate(models.Model):
    titulo = models.CharField(max_length = 50)
    link = models.CharField(max_length = 200)
    categoria = models.CharField(max_length = 50) 
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'bibliografía'

    def __str__ (self):
        template = '{0.titulo}, {0.categoria}'
        return template.format(self)
# Create your models here.
