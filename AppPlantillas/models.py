from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Mensaje(LoginRequiredMixin, models.Model):
    emisor = models.CharField(max_length=1200)
    receptor = models.CharField(max_length=1200)
    cuerpo = models.CharField(max_length=1200)
    tiempo = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    def __str__(self):
        return f"Asunto:{self.cuerpo}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=1200)
    subtitulo = models.CharField(max_length=1200)
    imagen = models.ImageField()
    cuerpo = models.CharField(max_length=1200)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Titulo:{self.titulo}"

class Profile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    website = models.URLField(max_length=200, blank=True)

    photo = models.ImageField(
        upload_to='pictures',
        blank=True,
        null=True
    )

    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
       
        return self.user.username        

class Blog(models.Model):
        
    title = models.CharField(max_length=255)
    content = RichTextField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)

class Image(models.Model):

    imagen = models.ImageField(
        upload_to='pictures',
        blank=True,
        null=True
    )

        