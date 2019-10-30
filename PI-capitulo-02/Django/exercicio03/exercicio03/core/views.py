from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialize
    name = 'profile-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialize
    name = 'profile-detail'


class AddressList(generics.ListCreateAPIView):
    queryset = Address
    serializer_class = AddresSerialize
    name = 'address-list'


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address
    serializer_class = AddresSerialize
    name = 'address-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post
    serializer_class = PostSerialize
    name = 'post-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post
    serializer_class = PostSerialize
    name = 'post-detail'


class CommentList(generics.ListCreateAPIView):
    queryset = Comment
    serializer_class = CommentSerialize
    name = 'comment-list'


class CommentDetail(generics.ListCreateAPIView):
    queryset = Comment
    serializer_class = CommentSerialize
    name = 'comment-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': reverse(ProfileList.name),
            'address': reverse(AddressList.name),
            'posts': reverse(PostList.name),
            'comments': reverse(CommentList.name),
        })