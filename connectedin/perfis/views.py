from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from perfis import session, constants
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# # 
# # Páginas
# # 
@login_required(login_url='login')
def index(request):
    perfil_logado = request.user.perfil

    return render(request, 'index.html', {
		'perfis': Perfil.objects.all(),
		'perfil_logado': perfil_logado
		})

@login_required(login_url='login')
def exibir_perfil(request, perfil_id):
    dados = {}
    dados['perfil'] = Perfil.objects.get(id=perfil_id)
    dados['perfil_logado'] = perfil_logado = request.user.perfil
    dados['ja_eh_contato'] = dados['perfil_logado'].contatos.filter(id=dados['perfil'].id)
    return render(request, 'perfil.html', dados)

@login_required(login_url='login')
def esqueci_a_minha_senha(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        query = Perfil.objects.filter(email=email)
        if len(query) == 0:
            messages.add_message(request, messages.INFO, 'Email não cadastrado')
            return redirect('esqueci_senha')
        else:
            # Deve criar um token
            # Deve enviar uma mensagem para o email do solicitante
            messages.add_message(request, messages.INFO, 'Ainda não feito, Um email foi enviado para você contendo o link de alteração de senha')
            return redirect('login')
    return render(request, 'esqueci_senha.html')

@login_required(login_url='login')
def postagem(request):
    return render(request, 'postagem.html')


# #
# # Métodos auxiliares
# #

@login_required(login_url='login')
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = request.user.perfil
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

@login_required(login_url='login')
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

@login_required(login_url='login')
def rejeitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.rejeitar()
    return redirect('index')

@login_required(login_url='login')
def desfazer_amizade(request, perfil_id):
    amizade = Perfil.objects.get(id=perfil_id)
    perfil_logado = request.user.perfil
    perfil_logado.desfazer_amizade(amizade)
    return redirect('index')

@login_required(login_url='login')
def alterar_senha(request):
    if request.method == 'POST':
        senha_antiga = request.POST.get('senha_antiga')
        nova_senha = request.POST.get('nova_senha')
        repete_senha = request.POST.get('repete_senha')

        # Alteração valida
        if dados_validos_para_alterar_senha(request, senha_antiga, nova_senha, repete_senha):
            perfil_logado.alterar_senha(nova_senha)
            return redirect('index')
        return redirect('alterar_senha')
    else:
        return render(request, 'alterarsenha.html')

@login_required(login_url='login')
def dados_validos_para_alterar_senha(request, senha_antiga, nova_senha, repete_senha):
    valido = True
    perfil_logado = request.user.perfil
    if senha_antiga != perfil_logado.senha:
        messages.add_message(request, messages.INFO, 'senha não confere com a cadastrada')
        valido = False
    if nova_senha != repete_senha:
        messages.add_message(request, messages.INFO, 'senha repetida não confere')
        valido = False
    return valido
