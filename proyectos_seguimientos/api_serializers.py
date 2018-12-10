from datetime import datetime

from rest_framework import serializers

from .models import Fase, TareaFase, FaseLiteral


class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fase
        fields = [
            'url',
            'id',
            'nombre'
        ]


class FaseLiteralSerializer(serializers.ModelSerializer):
    fase_nombre = serializers.CharField(source='fase.nombre', read_only=True)
    responsable_nombre = serializers.CharField(source='responsable.colaborador.full_name', read_only=True)
    nro_tareas = serializers.IntegerField(read_only=True)
    nro_tareas_terminadas = serializers.IntegerField(read_only=True)
    nro_tareas_vencidas = serializers.IntegerField(read_only=True)
    fecha_limite = serializers.DateField(read_only=True)

    class Meta:
        model = FaseLiteral
        fields = [
            'url',
            'id',
            'fase',
            'responsable_nombre',
            'responsable',
            'literal',
            'fase_nombre',
            'nro_tareas',
            'nro_tareas_terminadas',
            'nro_tareas_vencidas',
            'fecha_limite',
        ]


class TareaFaseSerializer(serializers.ModelSerializer):
    fecha_limite = serializers.DateTimeField(format="%Y-%m-%d", input_formats=['%Y-%m-%d', 'iso-8601'])
    vencido = serializers.SerializerMethodField()
    literal = serializers.IntegerField(source='fase_literal.literal.id', read_only=True)
    literal_id_literal = serializers.CharField(source='fase_literal.literal.id_literal', read_only=True)
    terminado = serializers.SerializerMethodField()
    estado_display = serializers.SerializerMethodField()
    asignado_a_nombre = serializers.CharField(source='asignado_a.colaborador.full_name', read_only=True)
    soy_asignado = serializers.BooleanField(read_only=True)
    soy_responsable = serializers.BooleanField(read_only=True)

    def get_terminado(self, obj):
        return obj.estado == 4

    def get_estado_display(self, obj):
        return obj.get_estado_display()

    def get_vencido(self, obj):
        try:
            return obj.fecha_limite < datetime.now().date() and not obj.estado == 4
        except TypeError:
            return False

    class Meta:
        model = TareaFase
        fields = [
            'url',
            'id',
            'asignado_a',
            'asignado_a_nombre',
            'soy_asignado',
            'soy_responsable',
            'fase_literal',
            'fecha_limite',
            'campo_uno',
            'campo_dos',
            'campo_tres',
            'literal',
            'literal_id_literal',
            'terminado',
            'descripcion',
            'estado',
            'estado_display',
            'vencido',
        ]
        extra_kwargs = {
            'campo_uno': {'required': False, 'allow_null': False, 'allow_blank': True},
            'campo_dos': {'required': False, 'allow_null': False, 'allow_blank': True},
            'campo_tres': {'required': False, 'allow_null': False, 'allow_blank': True},
        }
