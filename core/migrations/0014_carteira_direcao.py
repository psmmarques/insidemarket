# Generated by Django 3.2.5 on 2021-08-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_conversa'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteira',
            name='direcao',
            field=models.CharField(default='UP', max_length=100),
        ),
    ]