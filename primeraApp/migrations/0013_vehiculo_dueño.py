# Generated by Django 5.1.1 on 2024-11-17 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0012_remove_cita_servicio_cita_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='dueño',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primeraApp.cliente'),
        ),
    ]
