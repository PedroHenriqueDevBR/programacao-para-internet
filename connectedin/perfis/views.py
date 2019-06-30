from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite


# Create your views here.
def index(request):
    perfil_logado = get_perfil_logado(request)

    if len(perfil_logado) != 1:
        return redirect('login')

    return render(request, 'index.html', {
		'perfis': Perfil.objects.all(),
		'perfil_logado': perfil_logado
		})


def login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')

        usuario_cadastrado = 

        import pdb; pdb.set_trace()

    return render(request, 'login.html')


def exibir_perfil(request, perfil_id):
    dados = {}
    dados['perfil'] = Perfil.objects.get(id=perfil_id)
    dados['perfil_logado'] = get_perfil_logado(request)
    # import pdb; pdb.set_trace()
    dados['ja_eh_contato'] = dados['perfil_logado'].contatos.all()


    return render(request, 'perfil.html', dados)


def get(perfil_id):
    return Perfil.objects.get(id=perfil_id)


def get_perfil_logado(request):
    return Perfil.objects.filter(id=1)


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)

    return redirect('index')


def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')
