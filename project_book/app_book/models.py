from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username
    

class Book(models.Model):
    author = models.TextField()
    genre = models.TextField()
    title = models.TextField()
   
class Bookshelf(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='bookshelf')
    books = models.ManyToManyField(Book)


    
