# Generated by Django 2.0.4 on 2018-08-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0026_auto_20180822_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='fecha_limite_segumiento_estado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
