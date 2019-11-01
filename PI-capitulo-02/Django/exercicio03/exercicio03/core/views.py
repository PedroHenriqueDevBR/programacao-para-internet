from django.shortcuts import redirect
from rest_framework import generics
from .serializer import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
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
            'profile-posts': reverse(ProfilePostList.name, request=request),
            'posts-comments': reverse(PostCommentsList.name, request=request),
        })


# Classes da atividade

class ImportData(generics.GenericAPIView):
    name = 'import_data'

    def get(self, request, *args, **kwargs):
        self.import_data()
        return redirect(ApiRoot.name)

    def import_data(self):
        file = open('db.json')
        object = ''

        for line in file:
            object += line.strip()
        dict_json = json.loads(object)

        for user in dict_json['users']:
            pre_address = user['address']
            address = Address(street=pre_address['street'], suite=pre_address['suite'], city=pre_address['city'],
                              zipcode=pre_address['zipcode'])
            address.save()
            Profile.objects.create(name=user['name'], email=user['email'], address=address)

        for post in dict_json['posts']:
            user = Profile.objects.get(id=post['userId'])
            Post.objects.create(title=post['title'], body=post['body'], user=user)

        for comment in dict_json['comments']:
            post = Post.objects.get(id=comment['postId'])
            Comment.objects.create(name=comment['name'], email=comment['email'], body=comment['body'], post=post)


class ProfilePostList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerialize
    name = 'profile-post-list'


class ProfilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerialize
    name = 'profile-post-detail'


# class PostCommentsList(generics.GenericAPIView):
#     name = 'post-comments-list'
#
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         for post in posts:
#             post.comments.set(Comment.objects.filter(post=post))
#
#         return Response({
#             'posts': posts.__dict__()
#         }, status=status.HTTP_200_OK)


class PostCommentsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerialize
    name = 'post-comments-list'


class PostCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerialize
    name = 'post-comments-detail'