# Generated by Django 2.0.4 on 2018-05-30 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0016_auto_20180530_1701'),
        ('proyectos', '0034_auto_20180515_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='fecha_entrega_pactada',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='orden_compra_fecha',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='orden_compra_nro',
        ),
        migrations.AddField(
            model_name='literal',
            name='cotizacion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mi_cotizacion', to='cotizaciones.Cotizacion'),
        ),
    ]