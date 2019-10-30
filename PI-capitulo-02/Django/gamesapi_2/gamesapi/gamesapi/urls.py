from django.contrib import admin
from django.urls import path, include
from games import urls

urlpatterns = [
    path('games/', include(urls)),
    path('admin/', admin.site.urls),
]
