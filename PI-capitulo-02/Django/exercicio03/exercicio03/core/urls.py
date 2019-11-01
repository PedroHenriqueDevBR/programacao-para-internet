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

    # Rotas da atividade
    path('import/', ImportData.as_view(), name=ImportData.name),
    path('profile-posts/', ProfilePostList.as_view(), name=ProfilePostList.name),
    path('profile-posts/<int:pk>', ProfilePostDetail.as_view(), name=ProfilePostDetail.name),
    path('post-comments/', PostCommentsList.as_view(), name=PostCommentsList.name),
    path('post-comments/<int:pk>', PostCommentsDetail.as_view(), name=PostCommentsDetail.name),
]





