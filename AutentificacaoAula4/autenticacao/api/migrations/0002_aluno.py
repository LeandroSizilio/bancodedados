# Generated by Django 5.1.4 on 2025-01-16 00:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=10, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=11)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='conta_aluno', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
