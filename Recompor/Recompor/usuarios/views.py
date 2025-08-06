from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from composteira import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import Perfil  # ajuste para o local do seu modelo Perfil


def entrar(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        foto = request.POST.get("foto")  # <- Aqui capturamos a foto escolhida

        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            # Pode exibir uma mensagem de erro ou redirecionar
            return redirect("usuarios:logar")

        # Cria o usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        # Atualiza o perfil com a foto escolhida
        perfil = Perfil.objects.get(user=user)
        perfil.foto = foto  # <- Aqui atribuimos a foto escolhida
        perfil.save()

        return redirect("usuarios:logar")

    return render(request, "usuarios/cadastro.html")

        
        

def logar(request):
    if request.method == 'GET':
        return render(request, 'usuarios/Login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        #Função do django que autentica o usuário
        user = authenticate(username = username, password = senha)

        if user:
            login(request, user)
            #colocar Autenticado e renderizar a página do gráfico geral (com filtragem de composteira)
            composteiras = models.Composteira.objects.filter(fkUsuario_id = request.user)
            return render(request, "grafico-geral.html", {"composteiras": composteiras})

        else:
            #colocar mensagem que é preciso fazer o login 
            return render(request, "usuarios/login.html") 

# Função da deslogar usuário
def deslogar(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
def esqueceuSenha(request):
    if request.method == 'GET':
        return render(request, 'usuarios/Login.html')
    else:
     return render(request,"usuarios/Login.html")