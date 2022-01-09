# Generated by Django 3.2.9 on 2022-01-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('login', 'login'), ('etc', 'etc'), ('use', 'use'), ('report', 'report'), ('proposal', 'proposal')], max_length=80, null=True),
        ),
    ]
