from django.shortcuts import render, redirect, get_object_or_404
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
        vto = request.POST.get('vto', None)
        Post.objects.create(title=title, content=content, imagen=imagen, vto = vto)
        return redirect('inicio')
    
    return render(request, 'postear.html')

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        nueva_imagen = request.FILES.get('imagen')
        if nueva_imagen:
            post.imagen = nueva_imagen
        post.vto = request.POST.get('vto', None)

        post.save()
        return redirect('inicio')  

    return render(request, 'edit_post.html', {'post': post})