# Generated by Django 2.0.1 on 2018-03-27 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0021_remove_literal_costo_mano_obra'),
        ('cguno', '0035_colaboradorcostomesbiable_centro_costo'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaboradorbiable',
            name='literales_autorizados',
            field=models.ManyToManyField(related_name='colaboradores_autorizados', to='proyectos.Literal'),
        ),
    ]
