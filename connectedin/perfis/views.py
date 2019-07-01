from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from perfis import session, constants
from django.contrib import messages

# # 
# # Páginas
# # 
def index(request):
    perfil_logado = get_perfil_logado(request)

    if perfil_logado == None:
        return redirect('login')

    return render(request, 'index.html', {
		'perfis': Perfil.objects.all(),
		'perfil_logado': perfil_logado
		})


def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if logar(request, email, senha):
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Usuário não cadastrado')
        
    return render(request, 'login.html')


# #
# # Métodos auxiliares
# #

def exibir_perfil(request, perfil_id):
    dados = {}
    dados['perfil'] = Perfil.objects.get(id=perfil_id)
    dados['perfil_logado'] = get_perfil_logado(request)
    dados['ja_eh_contato'] = dados['perfil_logado'].contatos.filter(id=dados['perfil'].id)
    return render(request, 'perfil.html', dados)


def logar(request, email, senha):
    usuario = Perfil.objects.filter(email=email, senha=senha)
    logado_com_sucesso = len(usuario) == 1
    if logado_com_sucesso: session.adicionar_dado(request, constants.ID_USUARIO, str(usuario[0].id))
    return logado_com_sucesso


def deslogar(request):
    session.eliminar_dado(request, constants.ID_USUARIO)
    return redirect('index')


def get_perfil_logado(request):
    id_usuario = session.recuperar_dado(request, constants.ID_USUARIO)
    if id_usuario == '': return None
    return Perfil.objects.get(id=id_usuario)


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')


def rejeitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.rejeitar()
    return redirect('index')


def desfazer_amizade(request, perfil_id):
    amizade = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.desfazer_amizade(amizade)
    return redirect('index')


def alterar_senha(request):
    if request.method == 'POST':
        senha_antiga = request.POST.get('senha_antiga')
        nova_senha = request.POST.get('nova_senha')
        repete_senha = request.POST.get('repete_senha')

        # Valida alteração
        valido = True
        perfil_logado = get_perfil_logado(request)
        if senha_antiga != perfil_logado.senha:
            messages.add_message(request, messages.INFO, 'senha não confere com a cadastrada')
            valido = False
        if nova_senha != repete_senha:
            messages.add_message(request, messages.INFO, 'senha repetida não confere')
            valido = False

        # Alteração valida
        if valido:
            perfil_logado.alterar_senha(nova_senha)
            return redirect('index')
        else:
            return redirect('alterar_senha')
    else:
        return render(request, 'alterarsenha.html')