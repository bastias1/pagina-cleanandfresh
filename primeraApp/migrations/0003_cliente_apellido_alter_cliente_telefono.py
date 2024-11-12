# Generated by Django 5.1.1 on 2024-11-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeraApp', '0002_alter_empleado_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
