from django.contrib import admin
from django.urls import path
from games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', views.games_list),
    path('games/<int:id>', views.game_detail)
]
