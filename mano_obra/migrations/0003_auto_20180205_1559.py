# Generated by Django 2.0.1 on 2018-02-05 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cguno', '0009_auto_20180130_1733'),
        ('proyectos', '0009_auto_20180205_1432'),
        ('mano_obra', '0002_diatrabajo_diatrabajoop'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='diatrabajo',
            unique_together={('fecha', 'colaborador')},
        ),
        migrations.AlterUniqueTogether(
            name='diatrabajoop',
            unique_together={('dia', 'literal')},
        ),
    ]
