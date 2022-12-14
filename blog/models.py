from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Nombre')
    created =models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created' ]
        
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'titulo')
    content = models.TextField(verbose_name= 'contenido')
    published = models.DateTimeField(default= now, verbose_name='Fecha de publicacion')
    image = models.ImageField(verbose_name='imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias')
    created =models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created' ]
        
    def __str__(self):
        return self.title
        