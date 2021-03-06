# Generated by Django 2.0.4 on 2019-05-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas_eurobelt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDosComponenteBandaEurobelt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('nomenclatura', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='categoriacomponentebandaeurobelt',
            options={'permissions': [('list_categoriacomponentebandaeurobelt', 'Can see list categorias eurobelt')]},
        ),
        migrations.AlterModelOptions(
            name='colorbandaeurobelt',
            options={'permissions': [('list_colorbandaeurobelt', 'Can see list colores bandas eurobelt')]},
        ),
        migrations.AlterModelOptions(
            name='componentebandaeurobelt',
            options={'permissions': [('list_componentebandaeurobelt', 'Can see list componentes bandas eurobelt')]},
        ),
        migrations.AlterModelOptions(
            name='materialbandaeurobelt',
            options={'permissions': [('list_materialbandaeurobelt', 'Can see list materiales bandas eurobelt')]},
        ),
        migrations.AlterModelOptions(
            name='seriebandaeurobelt',
            options={'permissions': [('list_seriebandaeurobelt', 'Can see list series bandas eurobelt')]},
        ),
        migrations.AlterModelOptions(
            name='tipobandabandaeurobelt',
            options={'permissions': [('list_tipobandabandaeurobelt', 'Can see list tipos bandas eurobelt')]},
        ),
        migrations.RemoveField(
            model_name='categoriacomponentebandaeurobelt',
            name='factor_importacion',
        ),
        migrations.RemoveField(
            model_name='categoriacomponentebandaeurobelt',
            name='factor_importacion_aereo',
        ),
        migrations.RemoveField(
            model_name='categoriacomponentebandaeurobelt',
            name='margen_deseado',
        ),
        migrations.RemoveField(
            model_name='categoriacomponentebandaeurobelt',
            name='moneda',
        ),
    ]
