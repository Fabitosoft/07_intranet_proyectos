# Generated by Django 2.0.4 on 2019-04-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargues_catalogos', '0008_auto_20190411_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaboradorcatalogo',
            name='es_cguno',
        ),
        migrations.AddField(
            model_name='colaboradorcatalogo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
