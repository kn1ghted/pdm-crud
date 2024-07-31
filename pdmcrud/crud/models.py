from django.db import models

# Create your models here.
class User(models.Model):

    class Roles(models.TextChoices):
        ADMIN = 'AD', ('Administrator')
        EDITOR = 'ED', ('Editor')
        READER = 'RE', ('Reader')

    id = models.AutoField(primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=50, verbose_name='Username')
    password = models.CharField(max_length=255, verbose_name='Password')
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.READER, verbose_name='Role')
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.CharField(max_length=100, verbose_name='Email')
    address = models.TextField(max_length=200, verbose_name='Address')

    # Return string for user objects. Admin view list details
    def __str__(self):
        return self.username