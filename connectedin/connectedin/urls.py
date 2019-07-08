from django.contrib import admin
from django.urls import path
from perfis import views
from usuarios import views as view_usuario

urlpatterns = [
    # Principal
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    # auxiliar
    path('esqueciasenha/', views.esqueci_a_minha_senha, name='esqueci_senha'),

    # Perfil
    path('perfil/<int:perfil_id>/', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar/',views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer/',views.desfazer_amizade, name='desfazer'),
    path('perfil/<int:convite_id>/aceitar/',views.aceitar, name='aceitar'),
    path('perfil/<int:convite_id>/rejeitar/',views.rejeitar, name='rejeitar'),
    path('encontrar/', views.buscar_usuario, name='buscar_usuario'),
    path('conexoes/', views.conexoes, name='conexoes'),
    #Perfil Postagem,
    path('postagem/', views.postagem, name='postagem'),
    path('excluirpostagem/<int:id_postagem>', views.excluir_postagem, name='excluir_postagem'),

    # Usuarios
    path('registrar/', view_usuario.RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', view_usuario.LoginUsuarioView.as_view(), name='login'),
    path('deslogar/', view_usuario.logout_view, name='deslogar'),
    path('alterarsenha/', view_usuario.AlterarSenhaView.as_view(), name='alterar_senha'),
    path('tornarsuperuser/<int:id_perfil>', view_usuario.tornar_superuser, name='tornar_superuser'),
    path('retirarsuperuser/<int:id_perfil>', view_usuario.retirar_superuser, name='retirar_superuser'),
    path('bloquearuser/<int:id_perfil>', view_usuario.bloquear_usuario, name='bloquear_user'),
    path('desbloquearuser/<int:id_perfil>', view_usuario.desbloquear_usuario, name='desbloquear_user'),

]


