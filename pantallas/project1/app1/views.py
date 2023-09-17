from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    path = request.path
    post = Post.objects.all()
    return render (request, 'inicio.html',{'path':path,'post':post})

@login_required
def usuario(request):
    path = request.path
    return render (request, 'usuario.html',{'path':path})

@login_required
def servicio(request):
    path = request.path
    return render (request, 'servicio.html',{'path':path})

def mensaje(request):
    mensajes = request.path
    return HttpResponse(mensajes)

def crear_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        imagen = request.FILES['imagen'] if 'imagen' in request.FILES else None

        Post.objects.create(title=title, content=content, imagen=imagen)
        return redirect('inicio')
    
    return render(request, 'postear.html')