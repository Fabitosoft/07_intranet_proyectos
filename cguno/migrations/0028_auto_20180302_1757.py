# Generated by Django 2.0.1 on 2018-03-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cguno', '0027_auto_20180302_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradorbiable',
            name='paga_caja_compensacion',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='colaboradorbiable',
            name='paga_pension',
            field=models.BooleanField(default=True),
        ),
    ]
