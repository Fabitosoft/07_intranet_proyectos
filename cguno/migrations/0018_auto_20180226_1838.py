# Generated by Django 2.0.1 on 2018-02-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cguno', '0017_colaboradorbiable_nro_horas_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradorbiable',
            name='nro_horas_mes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]