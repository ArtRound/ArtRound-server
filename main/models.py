from django.db import models

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    useremail = models.EmailField(max_length=128)
    updated_at = models.DateTimeField(auto_now=True)


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
