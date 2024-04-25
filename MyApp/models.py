from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
import os
from uuid import uuid4
# Create your models here.





class CustomUser(AbstractUser):
    reset_token = models.CharField(max_length=100, blank=True, null=True)
    groups = models.ManyToManyField('auth.Group', related_name='myapp_users', blank=True, verbose_name='groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='myapp_users', blank=True, verbose_name='user permissions')





# Función para definir la ruta de carga de imágenes para cada banda
def image_upload_path(instance, filename):
    # Obtiene el nombre de la clase del modelo (ejemplo: Indio_Solari, La_renga, etc.)
    class_name = instance.__class__.__name__
    # Define la ruta de carga basada en el nombre de la banda y el nombre del archivo
    if class_name == 'Indio_Solari':
        return os.path.join('Indio_Solari', filename)
    elif class_name == 'La_renga':
        return os.path.join('La_Renga', filename)
    elif class_name == 'Divididos':
        return os.path.join('Divididos', filename)
    elif class_name == 'LasPelotas':
        return os.path.join('Las_Pelotas', filename)
    elif class_name == 'Ciro':
        return os.path.join('Ciro', filename)
    elif class_name == 'notvg':
        return os.path.join('ntvg', filename)


#para cargar las fotos 
# Modelo para Indio Solari
class Indio_Solari(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

    def __str__(self):
        return self.title

# Modelo para La Renga
class La_renga(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

    def __str__(self):
        return self.title

# Modelo para Divididos
class Divididos(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

    def __str__(self):
        return self.title

# Modelo para Ciro
class Ciro(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

    def __str__(self):
        return self.title

# Modelo para notvg
class notvg(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

    def __str__(self):
        return self.title

# Modelo para Las Pelotas
class LasPelotas(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

    def __str__(self):
        return self.title

        return ""
    
def image_upload_path(instance, filename):
    # Generar un nombre único para el archivo
    filename = f"{uuid4()}.{filename.split('.')[-1]}"
    # Devolver la ruta de destino para cargar la imagen
    return os.path.join('uploads/', filename)

class lugares(models.Model):
        lugar = models.CharField(max_length=100)
        fecha = models.DateField()
        hora = models.TimeField()
        descripcion = models.TextField()
        imagen = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

        def __str__(self):
            return self.lugar

class presentacion_divididos(models.Model):
        lugar = models.CharField(max_length=100)
        fecha = models.DateField()
        hora = models.TimeField()
        descripcion = models.TextField()
        imagen = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

        def __str__(self):
            return self.lugar
        
class presentacion_LaRenga(models.Model):
        lugar = models.CharField(max_length=100)
        fecha = models.DateField()
        hora = models.TimeField()
        descripcion = models.TextField()
        imagen = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

        def __str__(self):
            return self.lugar

class presentacion_Ciro(models.Model):
        lugar = models.CharField(max_length=100)
        fecha = models.DateField()
        hora = models.TimeField()
        descripcion = models.TextField()
        imagen = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

        def __str__(self):
            return self.lugar
        
class presentacion_LasPelotas(models.Model):
        lugar = models.CharField(max_length=100)
        fecha = models.DateField()
        hora = models.TimeField()
        descripcion = models.TextField()
        imagen = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

        def __str__(self):
            return self.lugar
        
class presentacion_ntvg(models.Model):
        lugar = models.CharField(max_length=100)
        fecha = models.DateField()
        hora = models.TimeField()
        descripcion = models.TextField()
        imagen = models.ImageField(upload_to=image_upload_path, null=True, blank=True)  

        def __str__(self):
            return self.lugar