from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    user_id = models.ForeignKey('User', related_name='review', on_delete=models.CASCADE, db_column='user_id')
    art_info_id = models.ForeignKey('ArtInfo', related_name='review', on_delete=models.CASCADE, db_column='art_info_id')
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    heart = models.IntegerField(blank=True)

class Question(models.Model):
    QUESTION_CHOICES = {
        ('report', 'report'), ('login', 'login'),
        ('use', 'use'), ('proposal', 'proposal'), ('etc', 'etc')
    }
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('User', related_name='question', on_delete=models.CASCADE, db_column='user_id')
    answer_id = models.ForeignKey('Answer', related_name='question', on_delete=models.CASCADE, db_column='answer_id')
    type = models.CharField(max_length=80, choices=QUESTION_CHOICES, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)

class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey('Question', related_name='answer', on_delete=models.CASCADE, db_column='question_id')
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)


class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class Favorites(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.TextField()
    end_time = models.TextField()
    art_info_id = models.ForeignKey('ArtInfo', related_name='favorites', on_delete=models.CASCADE, db_column='art_info_id')

class ArtInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    fcltyNm = models.TextField()
    weekdayOperOpenHhmm = models.TextField()
    weekdayOperColseHhmm = models.TextField()
    holidayOperOpenHhmm = models.TextField()
    holidayCloseOpenHhmm = models.TextField()
    rstdeInfo = models.TextField()
    adultChrge = models.TextField()
    yngbgsChrge = models.TextField()
    childChrge = models.TextField()
    rdnmadr = models.TextField()
    phoneNumber = models.TextField()
    homepageUrl = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()

class Visited(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    address = models.TextField()
    start_time = models.TextField()
    end_time = models.TextField()

class User(AbstractUser):
    username = None
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(default="", max_length=10)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(default="남자", blank=True, max_length=5)
    age = models.IntegerField(default=1, blank=True)
    profile_image = models.CharField(default="", blank=True, max_length=100)
    objects = CustomUserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin