# Generated by Django 2.0.4 on 2019-04-11 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_informacion_origen', '0003_sistemainformacionorigen_codigo_amarre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cargues_catalogos', '0003_auto_20190408_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargosCatalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cargo', models.PositiveIntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('tipo_cargo', models.CharField(blank=True, max_length=300, null=True)),
                ('sistema_informacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema_informacion_origen.SistemaInformacionOrigen')),
            ],
        ),
        migrations.CreateModel(
            name='ColaboradorCatalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('nombres', models.CharField(max_length=200, null=True)),
                ('apellidos', models.CharField(max_length=200, null=True)),
                ('porcentaje_caja_compensacion', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('porcentaje_pension', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('porcentaje_arl', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('porcentaje_salud', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('porcentaje_prestaciones_sociales', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('base_salario', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('auxilio_transporte', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('nro_horas_mes', models.PositiveIntegerField(default=0, null=True)),
                ('es_aprendiz', models.BooleanField(default=False)),
                ('en_proyectos', models.BooleanField(default=False)),
                ('es_cguno', models.BooleanField(default=False)),
                ('autogestion_horas_trabajadas', models.BooleanField(default=False)),
                ('es_salario_fijo', models.BooleanField(default=False)),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cargues_catalogos.CargosCatalogo')),
            ],
            options={
                'permissions': [('list_colaboradorcatalogo', 'Can see list colaboradores'), ('detail_colaboradorcatalogo', 'Can see detail colaborador')],
            },
        ),
        migrations.CreateModel(
            name='ColaboradorCentroCostoCatalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro_costo_id', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=120, unique=True)),
                ('centro_costo_padre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cargues_catalogos.ColaboradorCentroCostoCatalogo')),
                ('sistema_informacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema_informacion_origen.SistemaInformacionOrigen')),
            ],
            options={
                'permissions': [('list_colaboradorcentrocostocatalogo', 'Can see list centros costos colaboradores catalogo')],
            },
        ),
        migrations.CreateModel(
            name='ItemsCatalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_item', models.PositiveIntegerField()),
                ('id_referencia', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
                ('descripcion_dos', models.CharField(max_length=40)),
                ('activo', models.BooleanField(default=True)),
                ('nombre_tercero', models.CharField(max_length=120)),
                ('ultimo_costo', models.DecimalField(decimal_places=3, default=0, max_digits=18)),
                ('linea', models.CharField(max_length=120, null=True)),
                ('categoria_mercadeo', models.CharField(max_length=120, null=True)),
                ('categoria_mercadeo_dos', models.CharField(max_length=120, null=True)),
                ('categoria_mercadeo_tres', models.CharField(max_length=120, null=True)),
                ('serie', models.CharField(max_length=30, null=True)),
                ('ancho', models.CharField(max_length=60, null=True)),
                ('alto', models.CharField(max_length=60, null=True)),
                ('longitud', models.CharField(max_length=60, null=True)),
                ('diametro', models.CharField(max_length=60, null=True)),
                ('dientes', models.CharField(max_length=10, null=True)),
                ('material', models.CharField(max_length=100, null=True)),
                ('color', models.CharField(max_length=30, null=True)),
                ('desc_item_padre', models.CharField(max_length=40)),
                ('unidad_medida_inventario', models.CharField(max_length=6)),
                ('id_procedencia', models.CharField(max_length=1)),
                ('sistema_informacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema_informacion_origen.SistemaInformacionOrigen')),
            ],
        ),
        migrations.CreateModel(
            name='SucursalCatalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_sucursal', models.PositiveIntegerField()),
                ('nombre_establecimiento', models.CharField(max_length=200, null=True)),
                ('nombre_establecimiento_intranet', models.CharField(max_length=200, null=True)),
                ('cupo_credito', models.DecimalField(decimal_places=0, max_digits=10)),
                ('condicion_pago', models.PositiveIntegerField(null=True)),
                ('activo', models.BooleanField()),
                ('fecha_creacion', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='clientecatalogo',
            name='canal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresas', to='clientes.CanalDistribucion'),
        ),
        migrations.AlterField(
            model_name='clientecatalogo',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresas', to='clientes.GrupoCliente'),
        ),
        migrations.AlterField(
            model_name='clientecatalogo',
            name='industria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresas', to='clientes.TipoIndustria'),
        ),
        migrations.AddField(
            model_name='sucursalcatalogo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sucursales', to='cargues_catalogos.ClienteCatalogo'),
        ),
        migrations.AddField(
            model_name='sucursalcatalogo',
            name='sistema_informacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema_informacion_origen.SistemaInformacionOrigen'),
        ),
        migrations.AddField(
            model_name='colaboradorcatalogo',
            name='centro_costo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='colaboradores', to='cargues_catalogos.ColaboradorCentroCostoCatalogo'),
        ),
        migrations.AddField(
            model_name='colaboradorcatalogo',
            name='sistema_informacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistema_informacion_origen.SistemaInformacionOrigen'),
        ),
        migrations.AddField(
            model_name='colaboradorcatalogo',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ncolaborador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='sucursalcatalogo',
            unique_together={('sistema_informacion', 'nro_sucursal', 'cliente')},
        ),
        migrations.AlterUniqueTogether(
            name='itemscatalogo',
            unique_together={('sistema_informacion', 'id_item')},
        ),
        migrations.AlterUniqueTogether(
            name='colaboradorcentrocostocatalogo',
            unique_together={('sistema_informacion', 'centro_costo_id')},
        ),
        migrations.AlterUniqueTogether(
            name='cargoscatalogo',
            unique_together={('sistema_informacion', 'id_cargo')},
        ),
    ]
