from rest_framework import serializers

from .models import Proyecto, Literal


class LiteralSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='proyecto.cliente.nombre', read_only=True)
    proyecto_abierto = serializers.BooleanField(source='proyecto.abierto', read_only=True)
    id_proyecto = serializers.CharField(source='proyecto.id_proyecto', read_only=True)
    proyecto_nombre = serializers.CharField(source='proyecto.nombre', read_only=True)
    costo_mano_obra = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    costo_mano_obra_inicial = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    cantidad_horas_mano_obra = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    cantidad_horas_mano_obra_inicial = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    orden_compra_nro = serializers.CharField(source='cotizacion.orden_compra_nro', read_only=True)
    orden_compra_fecha = serializers.DateField(source='cotizacion.orden_compra_fecha', read_only=True)
    fecha_entrega_pactada = serializers.DateField(source='cotizacion.fecha_entrega_pactada', read_only=True)
    valor_cliente = serializers.DecimalField(source='cotizacion.valor_orden_compra', read_only=True,
                                             max_digits=20, decimal_places=2)
    cotizacion_nro = serializers.SerializerMethodField()
    cotizacion_fecha_entrega = serializers.DateField(source='cotizacion.fecha_entrega_pactada', read_only=True)

    def get_cotizacion_nro(self, obj):
        if obj.cotizacion:
            return '%s-%s' % (obj.cotizacion.unidad_negocio, obj.cotizacion.nro_cotizacion)
        return None

    class Meta:
        model = Literal
        fields = [
            'url',
            'id',
            'id_literal',
            'proyecto_abierto',
            'proyecto_nombre',
            'id_proyecto',
            'proyecto',
            'cliente_nombre',
            'abierto',
            'en_cguno',
            'descripcion',
            'costo_materiales',
            'costo_mano_obra',
            'costo_mano_obra_inicial',
            'cantidad_horas_mano_obra',
            'cantidad_horas_mano_obra_inicial',
            'proyecto',
            'orden_compra_nro',
            'orden_compra_fecha',
            'fecha_entrega_pactada',
            'valor_cliente',
            'cotizacion',
            'cotizacion_nro',
            'cotizacion_fecha_entrega',
        ]


class ProyectoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    orden_compra_nro = serializers.CharField(source='cotizacion.orden_compra_nro', read_only=True)
    orden_compra_fecha = serializers.DateField(source='cotizacion.orden_compra_fecha', read_only=True)
    fecha_entrega_pactada = serializers.DateField(source='cotizacion.fecha_entrega_pactada', read_only=True)

    costo_mano_obra = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    cantidad_horas_mano_obra = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    costo_mano_obra_inicial = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    cantidad_horas_mano_obra_inicial = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    cotizacion_nro = serializers.SerializerMethodField()
    costo_presupuestado = serializers.DecimalField(source='cotizacion.costo_presupuestado', read_only=True,
                                                   max_digits=20, decimal_places=2)
    valor_cliente = serializers.DecimalField(source='cotizacion.valor_orden_compra', read_only=True,
                                             max_digits=20, decimal_places=2)

    def get_cotizacion_nro(self, obj):
        if obj.cotizacion:
            return '%s-%s' % (obj.cotizacion.unidad_negocio, obj.cotizacion.nro_cotizacion)
        return None

    class Meta:
        model = Proyecto
        fields = [
            'url',
            'id',
            'id_proyecto',
            'abierto',
            'costo_materiales',
            'en_cguno',
            'costo_presupuestado',
            'costo_mano_obra',
            'costo_mano_obra_inicial',
            'cantidad_horas_mano_obra',
            'cantidad_horas_mano_obra_inicial',
            'cotizacion',
            'cotizacion_nro',
            'orden_compra_nro',
            'orden_compra_fecha',
            'fecha_entrega_pactada',
            'valor_cliente',
            'nombre',
            'cliente',
            'cliente_nombre',
        ]
        extra_kwargs = {'cliente': {'allow_null': True}}
