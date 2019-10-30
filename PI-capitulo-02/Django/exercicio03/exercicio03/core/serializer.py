from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import *


class AddresSerialize(HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode']


class CommentSerialize(HyperlinkedModelSerializer):
    # post = serializers.SlugRelatedField(Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'post']


class PostSerialize(HyperlinkedModelSerializer):
    # user = serializers.SlugRelatedField(Profile.objects.all(), slug_field='name')
    # comments = CommentSerialize(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'user', 'comments']


class ProfileSerialize(HyperlinkedModelSerializer):
    # address = serializers.SlugRelatedField(Address.objects.all(), slug_field='street')
    posts = PostSerialize(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['pk', 'name', 'email', 'address', 'posts']
