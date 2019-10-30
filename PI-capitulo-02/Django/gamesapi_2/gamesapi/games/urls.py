from django.urls import path
from games import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.GamesView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
