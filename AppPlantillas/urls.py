from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
 
    path('base/', base, name="Base"),
    path('prueba/', prueba, name="Prueba"),
    path('', principal, name="Principal"),
    path('pages/', noticias, name="noticias"),
    path('noticia_banfield/', noticia_banfield, name="noticia_banfield"),
    path('noticia_djokovic/', noticia_djokovic, name="noticia_djokovic"),
    path('noticia_pumas/', noticia_pumas, name="noticia_pumas"),
    path('seccionfutbol/', seccionfutbol, name="Seccionfutbol"),
    path('cargarmensaje/', cargarmensaje, name="cargarmensaje"),
    path('buscar/', buscar, name="buscar"),
    path('buscarmensaje/', buscarmensaje, name="buscarmensaje"),
    path('editarmensaje/', editarmensaje, name="editarmensaje"),
    path('cargarnoticia/', cargarnoticia, name="cargarnoticia"),
    path('about/', about, name="about"),
    path('login/', login_request, name = 'Login'),
    path('register/', register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='AppPlantillas/logout.html'), name='logout'),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),
    path('crearblog/', blog_and_photo_upload, name='crearblog'),
    path('blog/<int:blog_id>', view_blog, name='verblog'),
    path('listarblogs/', listarblogs, name='listarblogs'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)