from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige a alguna página de éxito o haz lo que necesites aquí
       
    return render(request, 'login.html')

def logout_view(request):
    logout(request)