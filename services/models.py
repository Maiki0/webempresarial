
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'titulo')
    subtitle = models.CharField(max_length=200, verbose_name= 'subtitulo')
    content = models.TextField(verbose_name='contenido')
    published = models.DateTimeField(default=now, verbose_name='Fecha de publicacion')
    image = models.ImageField(verbose_name='imagen', upload_to='services')
    created =models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicos'
        ordering = ['-created' ]
        
    def __str__(self):
        return self.title