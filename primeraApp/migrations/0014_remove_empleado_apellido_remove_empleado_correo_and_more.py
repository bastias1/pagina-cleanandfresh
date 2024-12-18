# Generated by Django 5.1.1 on 2024-11-17 18:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0013_vehiculo_dueño'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='password',
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
