# Generated by Django 2.0.1 on 2018-02-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cguno', '0016_auto_20180226_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradorbiable',
            name='nro_horas_mes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]