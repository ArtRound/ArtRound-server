# Generated by Django 3.2.6 on 2021-09-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('login', 'login'), ('use', 'use'), ('proposal', 'proposal'), ('report', 'report'), ('etc', 'etc')], max_length=80, null=True),
        ),
    ]