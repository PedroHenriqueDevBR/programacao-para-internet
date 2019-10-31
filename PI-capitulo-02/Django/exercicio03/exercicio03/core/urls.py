from django.urls import path
from .views import *


urlpatterns = [
    path('profile/', ProfileList.as_view(), name=ProfileList.name),
    path('profile/<int:pk>', ProfileDetail.as_view(), name=ProfileDetail.name),
    path('address/', AddressList.as_view(), name=AddressList.name),
    path('address/<int:pk>', AddressDetail.as_view(), name=AddressDetail.name),
    path('post/', PostList.as_view(), name=PostList.name),
    path('post/<int:pk>', PostDetail.as_view(), name=PostDetail.name),
    path('comment/', CommentList.as_view(), name=CommentList.name),
    path('comment/<int:pk>', CommentDetail.as_view(), name=CommentDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('import/', ImportData.as_view(), name=ImportData.name)
]





