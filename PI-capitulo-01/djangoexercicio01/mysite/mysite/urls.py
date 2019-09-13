"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pools import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:id>', views.question, name='question'),
    path('question/<int:id>/result', views.result, name='result'),
    path('question/<int:id>/vote', views.vote, name='vote'),
    path('question/<int:id>/manage', views.manage, name='manage'),
    path('question/close/<int:id_question>/manage/add/<int:id_choice>', views.add_choice, name='add_choice'),
    path('question/close/<int:id>', views.fechar_question, name='fechar_question'),
    path('choice/remove/<int:id>', views.remove_choice, name='remove_choice'),
]
