from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
import json


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialize
    name = 'profile-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerialize
    name = 'profile-detail'


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddresSerialize
    name = 'address-list'


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddresSerialize
    name = 'address-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialize
    name = 'post-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialize
    name = 'post-detail'


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialize
    name = 'comment-list'


class CommentDetail(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialize
    name = 'comment-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': reverse(ProfileList.name, request=request),
            'address': reverse(AddressList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'comments': reverse(CommentList.name, request=request),
        })


class ImportData(generics.GenericAPIView):
    name = 'import_data'

    def get(self, request, *args, **kwargs):
        self.import_data()
        print('Dados importados')

        return Response({
            'profile': reverse(ProfileList.name, request=request),
            'address': reverse(AddressList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'comments': reverse(CommentList.name, request=request),
        })


    def import_data(self):
        file = open('db.json')
        object = ''

        for line in file:
            object += line.strip()
        dict_json = json.loads(object)


        for user in dict_json['users']:
            pre_address = user['address']
            address = Address(street=pre_address['street'], suite=pre_address['suite'], city=pre_address['city'], zipcode=pre_address['zipcode'])
            address.save()
            Profile.objects.create(name=user['name'], email=user['email'], address=address)


        for post in dict_json['posts']:
            user = Profile.objects.get(id=post['userId'])
            Post.objects.create(title=title, body=body, user=user)


        for comment in dict_json['comments']:
            post = Post.objects.get(id=comment['postId'])
            Comment.objects.create(name=comment['name'], email=comment['email'], body=comment['body'], post=post)
