# Generated by Django 2.0.1 on 2018-03-26 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mano_obra', '0025_horahojatrabajo_autogestionada'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horahojatrabajo',
            options={'permissions': [('list_horahojatrabajo', 'Can see list horas trabajos diario'), ('verificar_horahojatrabajo', 'Can verificar horas trabajos diario')]},
        ),
    ]
