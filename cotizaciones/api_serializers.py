from rest_framework import serializers

from .models import Cotizacion, SeguimientoCotizacion


class CotizacionSerializer(serializers.ModelSerializer):
    responsable_nombres = serializers.CharField(source='responsable.first_name', read_only=True)
    responsable_apellidos = serializers.CharField(source='responsable.last_name', read_only=True)

    class Meta:
        model = Cotizacion
        fields = [
            'url',
            'id',
            'nro_cotizacion',
            'unidad_negocio',
            'cliente',
            'descripcion_cotizacion',
            'contacto',
            'estado',
            'observacion',
            'valor_ofertado',
            'valor_orden_compra',
            'costo_presupuestado',
            'responsable',
            'responsable_nombres',
            'responsable_apellidos',
        ]


class SeguimientoCotizacionSerializer(serializers.ModelSerializer):
    creado_por_username = serializers.CharField(source='creado_por.username', read_only=True)
    fecha_inicio_tarea = serializers.DateTimeField(
        format="%Y-%m-%d",
        input_formats=['%Y-%m-%d', 'iso-8601'],
        allow_null=True,
        required=False
    )
    fecha_fin_tarea = serializers.DateTimeField(
        format="%Y-%m-%d",
        input_formats=['%Y-%m-%d', 'iso-8601'],
        allow_null=True,
        required=False
    )

    class Meta:
        model = SeguimientoCotizacion
        fields = [
            'url',
            'id',
            'cotizacion',
            'tipo_seguimiento',
            'observacion',
            'estado',
            'nombre_tarea',
            'fecha_inicio_tarea',
            'fecha_fin_tarea',
            'tarea_terminada',
            'created',
            'modified',
            'creado_por_username',
            'creado_por',
        ]
        extra_kwargs = {
            'created': {'read_only': True},
            'modified': {'read_only': True},
            'creado_por': {'read_only': True},
        }
