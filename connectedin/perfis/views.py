from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite, Post
from perfis import session, constants
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# # 
# # Páginas
# # 
@login_required(login_url='login')
def index(request):
    dados = {}
    dados['perfis'] = Perfil.objects.all()
    dados['perfil_logado'] = request.user.perfil
    dados['timeline'] = selecionar_posts_de_amigos(request)

    return render(request, 'index.html', dados)

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
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')
        perfil = request.user.perfil

        Post.objects.create(titulo=titulo, text=texto, perfil=perfil)

        return redirect('index')

    return render(request, 'postagem.html')

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


# #
# # Métodos auxiliares
# #
def selecionar_posts_de_amigos(request):
    perfil_logado = request.user.perfil
    amigos = perfil_logado.contatos.all()
    posts = []
    
    for amigo in amigos:
        posts.extend(list(amigo.posts.all()))
    posts.sort(key=lambda x: x.data_postagem, reverse=True)

    return posts