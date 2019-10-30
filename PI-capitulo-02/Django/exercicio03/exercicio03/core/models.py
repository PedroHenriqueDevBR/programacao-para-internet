from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)


class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
