from django.db import models
from django.shortcuts import redirect

# Create your models here.
class User(models.Model):

    class Roles(models.TextChoices):
        ADMIN = 'administrator', ('Administrator')
        EDITOR = 'editor', ('Editor')
        READER = 'reader', ('Reader')

    id = models.AutoField(primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=50, verbose_name='Username')
    password = models.CharField(max_length=255, verbose_name='Password')
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.READER, verbose_name='Role')
    profile_picture = models.ImageField(upload_to='images/users/', verbose_name='Profile Picture', null=True),
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.CharField(max_length=100, verbose_name='Email')
    address = models.TextField(max_length=200, verbose_name='Address', null=True)

    # Return string for user objects. Admin view list details
    def __str__(self):
        return self.username
    
    # Delete profile pictures stored for users in images/users/
    # def delete(self, using=None, keep_parents=False):
    #     self.profile_picture.storage.delete(self.profile_picture.name)
    #     super.delete()