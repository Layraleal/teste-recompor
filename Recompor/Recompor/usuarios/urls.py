from django.urls import path
from . import views


app_name = "usuarios"

urlpatterns = [
    path("cadastro/", views.entrar, name = "entrar"),
    path("login/", views.logar, name = "logar"),
    path('deslogar/',views.deslogar,name='deslogar'),
    path("esqueceuSenha/",views.esqueceuSenha, name = "esqueceuSenha")


        
]










