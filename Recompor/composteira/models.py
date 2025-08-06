from django.db import models
from django.contrib.auth.models import User 
#from django.contrib.auth.models import User (User, verbose_name =  "usuário", on_delete = models.CASCADE)
from django.contrib.auth import get_user_model

#Aqui estão as tabelas composteiras e compostagens 

class Composteira(models.Model):
    id_composteira = models.BigAutoField(primary_key = True)
    fkUsuario = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    # com_minhoca = models.BooleanField(default=False, verbose_name="Com minhoca")
    REGIAO_CHOICE = (
        ("Norte","Norte"),
        ("Nordeste", "Nordeste"),
        ("Sul", "Sul"),
        ("Sudeste","Sudeste"),
        ("Centro-Oeste", "Centro-Oeste"),
    )
    regiao = models.CharField(max_length = 12, null = False, choices = REGIAO_CHOICE)
    TAMANHO_CHOICE = (
        ("Pequena","Pequena"),
        ("Média", "Média"),
        ("Grande", "Grande"),
    )
    tamanho = models.CharField(max_length = 7, null = False, choices = TAMANHO_CHOICE)

    TIPO_CHOICE = (

        ("Terra", "Terra"),
        ("Caixa", "Caixa" ),
    )
    tipo = models.CharField(max_length = 5, null = False, choices = TIPO_CHOICE)

    data_construcao = models.DateField(verbose_name="Data construção")
    nome = models.CharField(max_length = 50)


class Compostagem(models.Model):
    id_compostagem = models.BigAutoField(primary_key = True)
    fkComposteira = models.ForeignKey(Composteira, verbose_name =  "composteira", on_delete = models.CASCADE)
    fkUsuario_comp = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    data_inicio = models.DateField(verbose_name="Data colocado")
    # data_pronto = models.DateField(verbose_name="Data pronto")
    peso = models.FloatField()
