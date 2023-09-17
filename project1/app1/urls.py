from django.urls import path
from app1 import views

urlpatterns = [
   path('', views.inicio, name="inicio"),
   path('usuario', views.usuario,name="usuario"),
   path('servicio', views.servicio,name="servicio"),
   path('mensaje', views.mensaje,name="mensaje"),
   path('postear', views.crear_post,name="postear"),
   path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
