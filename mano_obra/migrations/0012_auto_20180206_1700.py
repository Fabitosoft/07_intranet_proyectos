# Generated by Django 2.0.1 on 2018-02-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mano_obra', '0011_horahojatrabajo_creado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='hojatrabajodiario',
            name='cantidad_horas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hojatrabajodiario',
            name='costo_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
