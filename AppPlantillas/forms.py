from tkinter import PhotoImage
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from AppPlantillas.models import Blog, Image

class formulario_mensaje(forms.Form):
    emisor = forms.CharField()
    receptor = forms.CharField()
    cuerpo = forms.CharField()


class formulario_noticia(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField()
    imagen=forms.ImageField()
    cuerpo = forms.CharField()


class mensajeleido(forms.Form):
    leido=forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['imagen']
    
    
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']        