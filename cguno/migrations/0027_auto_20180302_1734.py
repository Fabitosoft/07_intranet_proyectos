# Generated by Django 2.0.1 on 2018-03-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cguno', '0026_auto_20180302_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradorcostomesbiable',
            name='lapso',
            field=models.DateField(),
        ),
        migrations.AlterUniqueTogether(
            name='colaboradorcostomesbiable',
            unique_together={('lapso', 'colaborador')},
        ),
    ]
