from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from AppPlantillas.forms import *
from AppPlantillas.models import *

def base(request):

    return render(request, "AppPlantillas/base.html")

def prueba(request):

    return render(request, "AppPlantillas/template.html")

def principal(request):

    return render(request, "AppPlantillas/index.html")
    
def noticias(request):

    return render(request, "AppPlantillas/noticias.html")

def noticia_banfield(request):

    return render(request, "AppPlantillas/noticia_banfield.html")

def noticia_djokovic(request):

    return render(request, "AppPlantillas/noticia_djokovic.html")

def noticia_pumas(request):

    return render(request, "AppPlantillas/noticia_pumas.html")

def seccionfutbol(request):

    return render(request, "AppPlantillas/seccion_futbol.html")

def about(request):

    return render(request, "AppPlantillas/about.html")


@login_required
def cargarmensaje(request):
    if (request.method=="POST"):
        form=formulario_mensaje(request.POST)
        print(form) 
        if form.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= form.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            emisor=info["emisor"]
            receptor=info["receptor"]
            cuerpo=info["cuerpo"]
            msg= Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo, leido=0)
            msg.save()
            return render (request, "AppPlantillas/index.html")
    else: #Si no viene por POST
        form=formulario_mensaje() #Creo el formulario vacio
    return render(request, "AppPlantillas/formulariomensaje.html", {"form":form})##lo renderizo y se lo mando como un diccionario para que lo pueda usar mi pantalla, mi template, como una variable.
    ##formulario de arriba tiene que ser el mismo que aparece en el html para usar

@login_required
def buscarmensaje(request):
    return render(request, "AppPlantillas/buscarmensaje.html")

@login_required
def buscar(request):
    if request.GET["receptor"]:
        receptor=request.GET["receptor"]
        mensaje=Mensaje.objects.filter(receptor=receptor,leido=0)
        return render(request, "AppPlantillas/resultadomensaje.html", {"receptor":receptor, "mensaje":mensaje})

    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

def editarmensaje(request, receptor):
    mensaje=Mensaje.objects.get(receptor=receptor)
    if request.method=="POST":
        formu=formulario_mensaje(request.POST)
        if formu.is_valid():
            info=formu.cleaned_data
            mensaje.leido=info["leido"]
            mensaje.save()
            return render (request, "AppPlantillas/index.html")

    else:
        formu= mensajeleido(initial={"leido":mensaje.leido})
    return render(request, "AppPlantillas/editarmensaje.html",{"formulario":formu})
            

   
def cargarnoticia(request):
    if (request.method=="POST"):
        formu_noticia=formulario_noticia(request.POST)
        print(formu_noticia) 
        if formu_noticia.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= formu_noticia.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            titulo=info["titulo"]
            subtitulo=info["subtitulo"]
            imagen=info["imagen"]
            cuerpo=info["cuerpo"]
            msg= Noticia(titulo=titulo, subtitulo=subtitulo, imagen=imagen, cuerpo=cuerpo)
            msg.save()
            return render (request, "AppPlantillas/index.html")
    else: #Si no viene por POST
        formu_noticia=formulario_noticia() #Creo el formulario vacio
    return render(request, "AppPlantillas/formulariomensaje.html", {"form":formu_noticia})##lo renderizo y se lo mando como un diccionario para que lo pueda usar mi pantalla, mi template, como una variable.
    ##formulario de arriba tiene que ser el mismo que aparece en el html para usar

def login_request(request):

        if request.method == "POST":
           form = AuthenticationForm(request, data = request.POST)

           if form.is_valid():
                 usuario = form.cleaned_data.get('username')
                 contra = form.cleaned_data.get('password')

                 user = authenticate(username=usuario, password=contra)

                 if user is not None:
                       login(request, user)
                       return render(request, "AppPlantillas/login.html", {"mensaje":f"Bienvenido {usuario}"} )
                 else:
                        return render(request,"AppPlantillas/index.html", {"mensaje":"Error, datos incorrectos"} )
           else:  
                        return render(request,"AppPlantillas/index.html", {"mensaje":"Error, formulario erroneo"})

        form = AuthenticationForm()

        return render(request,"AppPlantillas/login.html", {'form':form} )

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)      
        if form.is_valid():
             username = form.cleaned_data['username']

             form.save()
             return render(request,"AppPlantillas/index.html" , {"mensaje":"Usuario creado correctamente"})

    else:
        form = UserRegisterForm()
    return render(request,"AppPlantillas/register.html" , {"form":form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        editarPerfil = UserEditForm(request.POST)

        print(editarPerfil)

        if editarPerfil.is_valid:

            informacion = editarPerfil.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "AppPlantillas/index.html")

    else:

          editarPerfil= UserEditForm(initial={ 'email':usuario.email})

    return render(request, "AppPlantillas/editarPerfil.html", {"editarPerfil":editarPerfil, "usuario":usuario})           

@login_required
def blog_and_photo_upload(request):
    blog_form = BlogForm()
    photo_form = PhotoForm()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('crearblog')
    context = {
       'blog_form': blog_form,
       'photo_form': photo_form,
   }
    return render(request, 'AppPlantillas/crearblog.html', context=context)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'AppPlantillas/verblog.html', {'blog': blog})

def listarblogs(request):
    photos = Image.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'AppPlantillas/listarblogs.html', context={'photos': photos, 'blogs': blogs})




