from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(verbose_name='Nombre', max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['-created']
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    published=models.DateTimeField(verbose_name='Publicacion',default=now())
    image=models.ImageField(verbose_name='Imagen', upload_to='blog',blank=True, null=True)
    author=models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category, verbose_name='Categorias')
    created=models.DateTimeField(verbose_name='Creacion', auto_now_add=True)
    updated=models.DateTimeField(verbose_name='Modificacion', auto_now=True)
    
    class Meta:
        verbose_name='Posteo'
        verbose_name_plural='Posteos'
        ordering=['-published']
    def __str__(self):
        return self.title
    