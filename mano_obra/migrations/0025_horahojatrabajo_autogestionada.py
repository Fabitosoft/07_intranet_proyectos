# Generated by Django 2.0.1 on 2018-03-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mano_obra', '0024_auto_20180322_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='horahojatrabajo',
            name='autogestionada',
            field=models.BooleanField(default=False),
        ),
    ]
