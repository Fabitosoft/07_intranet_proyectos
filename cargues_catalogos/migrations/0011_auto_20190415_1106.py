# Generated by Django 2.0.4 on 2019-04-15 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargues_catalogos', '0010_auto_20190415_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sucursalcatalogo',
            old_name='nombre_establecimiento_intranet',
            new_name='nombre_establecimiento_alternativo',
        ),
    ]