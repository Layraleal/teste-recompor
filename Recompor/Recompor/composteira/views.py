from django.shortcuts import render
from django.http import HttpResponse
from .models import Composteira
from .models import Compostagem
from usuarios import *
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.db.models import Subquery, OuterRef
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import ComposteiraForm



def viewAdicionarComposteira(request):
    #Verifica se o user está logado
    if request.user.is_authenticated == True:
        #Verifica se o metodo é o get e não o post
        if request.method == 'GET': 
            return render(request, "addComposteira.html")
        #Captura os dados e salva e renderiza para outra tela
        else:
            name_comp = request.POST.get("name_comp")
            data_const = request.POST.get("data_const")
            escala = request.POST.get("escala_comp")
            regiao = request.POST.get("regiao")
            tipo = request.POST.get("tipo")
            composteira = Composteira(fkUsuario = request.user, regiao = regiao, tamanho = escala, tipo = tipo, data_construcao = data_const, nome = name_comp)
            composteira.save()
            context = {
                'nomeUser': request.user.username
            }
            composteiras = Composteira.objects.filter(fkUsuario_id = request.user)
            return render(request, "grafico-geral.html", {"composteiras": composteiras})
    return render(request, "usuarios/Login.html") 


def viewAdicionarCompostagem(request):
    if request.user.is_authenticated == True:
        if request.method == 'GET': 
            composteiras = Composteira.objects.filter(fkUsuario_id = request.user)
            return render(request, "addCompostagem.html", {"composteiras": composteiras})
        else:
            data_inicio = request.POST.get("data_inicio")
            #data_pronto = request.POST.get("data_pronto")
            fkComposteira = request.POST.get("composteira")
            peso = request.POST.get("peso")
            compostagem = Compostagem(fkComposteira = Composteira.objects.get(id_composteira=fkComposteira), data_inicio = data_inicio, peso=peso, fkUsuario_comp = request.user)
            compostagem.save()

            composteiras = Composteira.objects.filter(fkUsuario=request.user)
            compostagens = Compostagem.objects.filter(fkUsuario_comp=request.user, fkComposteira__in=composteiras)
            return render(request, "graficoIndiv.html", {"compostagens": compostagens, "composteiras": composteiras})
    return render(request, "usuarios/Login.html") 
    

def viewGraficoGeral(request):
    #Filtra as composteiras de acordo com o usuario
    if request.user.is_authenticated == True:
        composteiras = Composteira.objects.filter(fkUsuario_id = request.user)
        return render(request, "grafico-geral.html", {"composteiras": composteiras})
    return render(request, "usuarios/Login.html") 


def Emissao(request):
    if request.user.is_authenticated:
        #Filtra as composteiras associadas ao usuário
        composteiras_usuario = Composteira.objects.filter(fkUsuario=request.user)
        #Lista para armazenar os resultados
        resultados = []
        for composteira in composteiras_usuario:
            #Filtra as compostagens associadas à composteira e ao usuário
            peso_compostagem = (
                Compostagem.objects
                .filter(fkComposteira=composteira)
                .annotate(mes=ExtractMonth('data_inicio'))
                .values('mes')
                .annotate(soma_peso=Sum('peso'))
                .order_by('mes')
            )

            #Loop para iterar sobre os resultados da compostagem
            for resultado in peso_compostagem:
                mes = resultado['mes']
                soma_peso = resultado['soma_peso']
                emissao_real = f'Composteira: {composteira.nome}, Mês: {mes}, Soma do Peso: {0.084 * soma_peso}'
                #Adiciona o resultado à lista
                resultados.append(emissao_real)

        #Une os resultados em uma única string com quebras de linha HTML
        resposta = '\n'.join(resultados)
        #Retorna a resposta HTTP com todos os resultados
        return HttpResponse(resposta)


def GraficoIndividualView(request):
    # Obtém todas as composteiras do usuário atual
    composteiras = Composteira.objects.filter(fkUsuario=request.user)

    # Filtra as compostagens com base no usuário atual e em todas as composteiras obtidas
    compostagens = Compostagem.objects.filter(fkUsuario_comp=request.user, fkComposteira__in=composteiras)

    # Passe as compostagens e todas as composteiras para o template
    return render(request, "graficoIndiv.html", {"compostagens": compostagens, "composteiras": composteiras})


#def vieweditarComposteira(request, id_composteira):
    if request.user.is_authenticated:
        composteira = get_object_or_404(Composteira, id_composteira=id_composteira, fkUsuario=request.user)
        
        if request.method == 'POST':
            form = ComposteiraForm(request.POST, instance=composteira)
            if form.is_valid():
                form.save()
                messages.success(request, 'Composteira atualizada com sucesso!')
                return redirect('composteira:graficoGeral')
            else:
                messages.error(request, 'Por favor, corrija os erros abaixo.')
        else:
            form = ComposteiraForm(instance=composteira)
        
        return render(request, 'editarComposteira.html', {'form': form, 'composteira': composteira})
    else:
        return redirect('usuarios:login') #nao da certo esse def


def vieweditarComposteira(request, id_composteira):
    # Verifica se o user está logado
    if request.user.is_authenticated:
        try:
            # Tenta obter a composteira pelo id_composteira e do usuário logado
            composteira = Composteira.objects.get(id_composteira=id_composteira, fkUsuario=request.user)
        except Composteira.DoesNotExist:
            return render(request, "erro.html", {"mensagem": "Composteira não encontrada"})


        if composteira.fkUsuario == request.user:    
            if request.method == 'GET':
                # Passa a composteira para o template
                return render(request, "editarComposteira.html", {"composteira": composteira})
            elif request.method == "POST":
                # Captura os dados do POST e atualiza a composteira
                composteira.nome = request.POST.get("name_comp")
                composteira.data_construcao = request.POST.get("data_const")
                composteira.tamanho = request.POST.get("escala_comp")
                composteira.regiao = request.POST.get("regiao")
                composteira.tipo = request.POST.get("tipo")
                composteira.save()
                composteiras = Composteira.objects.filter(fkUsuario_id=request.user)
                return render(request, "grafico-geral.html", {"composteiras": composteiras})
        return render(request, "usuarios/Login.html")
    
    
def viewexcluirComposteira(request, id_composteira):
    # Obtém a composteira com o id especificado
    composteira = get_object_or_404(Composteira, id_composteira=id_composteira)
    if request.method == 'POST':
        # Se a requisição for um POST, exclui a composteira
        composteira.delete()
        # Adiciona uma mensagem de sucesso informando que a composteira foi excluída com sucesso
        messages.success(request, 'Composteira excluída com sucesso!')
        # Redireciona o usuário para a página geral de gráficos das composteiras
        return redirect('composteira:graficoGeral')

    # Se a requisição for um GET, renderiza o template 'excluirComposteira.html'
    # passando a composteira para ser exibida na confirmação de exclusão
    return render(request, 'excluirComposteira.html', {'composteira': composteira})
