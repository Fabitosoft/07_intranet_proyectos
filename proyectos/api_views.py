from django.db.models import Sum, Value as V, F, ExpressionWrapper, DecimalField, OuterRef, Subquery
from django.db.models.expressions import RawSQL
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Proyecto, Literal
from .api_serializers import ProyectoSerializer, LiteralSerializer
from mano_obra.models import HojaTrabajoDiario, HoraHojaTrabajo


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        mano_obra = HoraHojaTrabajo.objects.values('literal__proyecto__id_proyecto').annotate(
            cantidad_horas=ExpressionWrapper(Sum((F('cantidad_minutos') / 60)),
                                             output_field=DecimalField(max_digits=4)),
            costo_total=ExpressionWrapper(
                Sum((F('cantidad_minutos') / 60) * (F('hoja__tasa__costo') / F('hoja__tasa__nro_horas_mes'))),
                output_field=DecimalField(max_digits=4))
        ).filter(
            literal__proyecto__id_proyecto=OuterRef('id_proyecto')
        )
        qs = Proyecto.objects.prefetch_related(
            'mis_literales'
        ).annotate(costo_mano_obra=Subquery(mano_obra.values('costo_total')),
                   cantidad_horas_mano_obra=Subquery(mano_obra.values('cantidad_horas')))
        return qs

    @list_route(http_method_names=['get', ])
    def abiertos(self, request):
        lista = self.get_queryset().filter(abierto=True).all()
        serializer = self.get_serializer(lista, many=True)
        return Response(serializer.data)


class LiteralViewSet(viewsets.ModelViewSet):
    queryset = Literal.objects.select_related(
        'proyecto'
    ).all()
    serializer_class = LiteralSerializer

    def get_queryset(self):
        mano_obra = HoraHojaTrabajo.objects.values('literal').annotate(
            cantidad_horas=ExpressionWrapper(Sum((F('cantidad_minutos') / 60)),
                                             output_field=DecimalField(max_digits=4)),
            costo_total=ExpressionWrapper(
                Sum((F('cantidad_minutos') / 60) * (F('hoja__tasa__costo') / F('hoja__tasa__nro_horas_mes'))),
                output_field=DecimalField(max_digits=4))
        ).filter(
            literal_id=OuterRef('id')
        )

        qs = Literal.objects.select_related(
            'proyecto'
        ).annotate(costo_mano_obra=Subquery(mano_obra.values('costo_total')),
                   cantidad_horas_mano_obra=Subquery(mano_obra.values('cantidad_horas')))
        return qs

    @list_route(http_method_names=['get', ])
    def abiertos(self, request):
        lista = self.get_queryset().filter(proyecto__abierto=True).all()
        serializer = self.get_serializer(lista, many=True)
        return Response(serializer.data)

    @list_route(http_method_names=['get', ])
    def listar_x_proyecto(self, request):
        proyecto_id = request.GET.get('proyecto_id')
        qs = None
        if proyecto_id:
            qs = self.get_queryset().filter(proyecto_id=proyecto_id)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
