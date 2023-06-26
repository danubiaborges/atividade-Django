from datetime import datetime  #biblioteca python para trabalhar com datas
import random #biblioteca python para gerar numeros aleatorios
from http import client #biblioteca python para fazer conexão com um nó cliente. Esse nó seria o navegador do usuário final do nosso sistema
from django.shortcuts import render #biblioteca do django para enviar respostas usando o protocolo http
from django.shortcuts import redirect #biblioteca do django para redirecionar de uma interface web (página web) para outra - cria a navegação entre páginas web
from django.http import HttpResponse
from django.utils import timezone

#importações dos modelos (classes) necessários para o UC Abrir Conta
#from ItaCar_app.models import contaComum, PessoaFisica

# Inicio dos métodos que compõem o fluxo de controle a partir da interação do usuário com as interfaces web (página html).

def home(request):
    #método executado quando o usuário está na interface (paǵina html) inicial do sistema  home.html
    return render(request, "ItaCar/home.html")

def efetuarLogin(request):
    return render(request, "ItaCar/efetuarLogin.html")

def avaliarPassageiro(request):
    if request.method == 'POST':
        idCorrida = request.POST.get('idCorrida')
        nomePass = request.POST.get('nomePass')
        nota = request.POST.get('nota')
        comentario = request.POST.get('comentario')
    
    return render(request, "ItaCar/avaliarPassageiro.html")