# Generated by Django 2.0.4 on 2018-05-07 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cotizacion',
            options={'permissions': [['list_cotizacion', 'Puede listar cotizaciones'], ['detail_cotizacion', 'Puede ver detalle cotizacion']]},
        ),
    ]
