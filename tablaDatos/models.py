from django.db import models

class SocialPackItem(models.Model):
    link = models.CharField(max_length=30)
    active = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)


class SocialPack(models.Model):
     socialPack = models.CharField(max_length=30)
   # socialPack = models.ManyToManyField(SocialPackItem)

class UserData(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    #socialPack = models.ForeignKey(SocialPack, on_delete=models.CASCADE)
