# Generated by Django 2.0.4 on 2018-05-31 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0035_auto_20180530_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literal',
            name='cotizacion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mi_literal', to='cotizaciones.Cotizacion'),
        ),
    ]
