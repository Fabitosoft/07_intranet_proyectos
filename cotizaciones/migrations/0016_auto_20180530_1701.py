# Generated by Django 2.0.4 on 2018-05-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0015_cotizacion_orden_compra_nro'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='fecha_entrega_pactada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='orden_compra_fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
