from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import RegistrarUsuarioForm
from perfis.models import Perfil
from django.contrib import messages

# Create your views here.
class RegistrarUsuarioView(View):
    template_name = 'usuarios/registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            usuario = User.objects.create_user(username=dados_form['nome'],
                                                email=dados_form['email'],
                                                password=dados_form['senha'])

            perfil = Perfil(nome=dados_form['nome'],
                            telefone=dados_form['telefone'],
                            nome_empresa=dados_form['nome_empresa'],
                            usuario=usuario)
            perfil.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class LoginUsuarioView(View):
    template_name = 'usuarios/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('user')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.add_message(request, messages.INFO, 'Usuário não cadastrado.')
            login(request, user)
        else:
            messages.add_message(request, messages.INFO, 'Logado com sucesso.')

        return redirect('login')
