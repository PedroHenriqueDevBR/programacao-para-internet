from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'index.html', {
		'perfis': Perfil.objects.all(),
		'perfil_logado': get_perfil_logado(request)
		})


def exibir_perfil(request, perfil_id):
    dados = {}
    dados['perfil'] = Perfil.objects.get(id=perfil_id)
    dados['perfil_logado'] = get_perfil_logado(request)
    # import pdb; pdb.set_trace()
    dados['ja_eh_contato'] = dados['perfil_logado'].contatos.all()


    return render(request, 'perfil.html', dados)


def get(perfil_id):
    return Perfil.objects.get(id=perfil_id)


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)

    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)


def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')
