# Generated by Django 2.1.3 on 2018-11-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comando', models.CharField(max_length=100)),
                ('saida', models.TextField()),
                ('code', models.TextField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]