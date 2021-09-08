from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Element, Handbook
from api.serializers import ElementSerializer, HandbookSerializer
from api.utils import format_version


class HandbookViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение всех справочников."""
    queryset = Handbook.objects.all()
    serializer_class = HandbookSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = HandbookFilter
    filterset_fields = ('title',)

    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save(version=format_version(data['version']))


class ElementViewSet(viewsets.ReadOnlyModelViewSet):
    """ Получение элементов заданного справочника текущей версии или указанной версии."""
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ElementFilter
    filterset_fields = ('handbook', 'version',)

class ValidateViewSet(viewsets.ReadOnlyModelViewSet):
    """Проверка наличия элементов заданного справочника текущей версии или указанной версии
        Возвращает null если элемент не найден. """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ValidateFilter
    filterset_fields = ('handbook', 'version', 'el_code', 'el_value')