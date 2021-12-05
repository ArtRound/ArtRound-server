from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    useremail = models.EmailField(max_length=128, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

class Question(models.Model):
    QUESTION_CHOICES = {
        ('report', 'report'), ('login', 'login'),
        ('use', 'use'), ('proposal', 'proposal'), ('etc', 'etc')
    }
    useremail = models.EmailField(max_length=128)
    type = models.CharField(max_length=80, choices=QUESTION_CHOICES, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)

class Answer(models.Model):
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)


class Notice(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class Favorites(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin