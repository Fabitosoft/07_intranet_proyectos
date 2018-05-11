# Generated by Django 2.0.4 on 2018-05-07 17:19

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0002_auto_20180507_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeguimientoCotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('tipo_seguimiento', models.PositiveIntegerField(choices=[(0, 'Comentario'), (1, 'Cambio de Estado'), (2, 'Tarea')])),
                ('observacion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=200, null=True)),
                ('nombre_tarea', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_inicio_tarea', models.DateField(blank=True, null=True)),
                ('fecha_fin_tarea', models.DateField(blank=True, null=True)),
                ('tarea_terminada', models.BooleanField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
