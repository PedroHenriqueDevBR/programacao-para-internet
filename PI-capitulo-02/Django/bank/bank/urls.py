from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', account_list),
    path('accounts/<int:pk>', account_detail)
]
