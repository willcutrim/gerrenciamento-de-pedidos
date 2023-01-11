from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as logout_django, login as login_django


def cadastro_usuario(request):
    
    if request.method == 'POST':
        try:
            usuario_exists = User.objects.get(email=request.POST.get('email'))
            if usuario_exists:
                return 'usuario ja existe'
        except User.DoesNotExist:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            

            novo_usuario = User.objects.create_user(username=username, email=email, password=password)

            novo_usuario.save()
            return redirect('/produtos/')
            
        
    return render(request, 'html/cadastro_usuario.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('/produtos/')
        else:
            return HttpResponse('email ou senha invalida')
    return render(request, 'html/login.html')


@login_required(login_url="/usuario/login/")
def logout(request):
    if request.user.is_authenticated:
        logout_django(request)
        return redirect('login/')
