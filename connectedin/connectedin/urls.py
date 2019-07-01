from django.contrib import admin
from django.urls import path
from perfis import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('deslogar/', views.deslogar,name='deslogar'),
    path('perfil/<int:perfil_id>', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar',views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer',views.desfazer_amizade, name='desfazer'),
    path('perfil/<int:convite_id>/aceitar',views.aceitar, name='aceitar'),
    path('perfil/<int:convite_id>/rejeitar',views.rejeitar, name='rejeitar'),
]


