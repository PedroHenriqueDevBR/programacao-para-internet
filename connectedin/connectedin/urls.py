from django.contrib import admin
from django.urls import path
from perfis import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    path('login/', views.login, name='login'),
    path('deslogar/', views.deslogar, name='deslogar'),
    path('alterarsenha/', views.alterar_senha, name='alterar_senha'),
    path('esqueciasenha/', views.esqueci_a_minha_senha, name='esqueci_senha'),

    path('postagem/', views.postagem, name='postagem'),

    path('perfil/<int:perfil_id>/', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar/',views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer/',views.desfazer_amizade, name='desfazer'),
    path('perfil/<int:convite_id>/aceitar/',views.aceitar, name='aceitar'),
    path('perfil/<int:convite_id>/rejeitar/',views.rejeitar, name='rejeitar'),
]


