from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, Page



# Create your views here.

def inicio(request):
    search_query = request.GET.get('buscar', '')

    if search_query:
        post_list = Post.objects.filter(title__icontains=search_query)
    else:
        post_list = Post.objects.all()

    paginator = Paginator(post_list, 5)  

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'inicio.html', {'page': page, 'search_query': search_query})


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

@login_required
def crear_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        imagen = request.FILES['imagen'] if 'imagen' in request.FILES else None
        vto = request.POST.get('vto', None)
        Post.objects.create(title=title, content=content, imagen=imagen, vto = vto)
        return redirect('inicio')
    
    return render(request, 'postear.html')

@login_required
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