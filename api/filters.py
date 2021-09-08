from django_filters import rest_framework as filters
from api.models import Handbook, Element


class VersionHandbook(filters.FilterSet):
    date = filters.DateFilter(field_name='version__start_date', lookup_expr='lte')

    class Meta:
        model = Handbook
        fields = ('date',)


class ElementFilter(filters.FilterSet):
    catalog = filters.CharFilter(field_name='handbook__title',
                                 lookup_expr='contains')
    version = filters.CharFilter(field_name='handbook__version',
                                 lookup_expr='exact')

    class Meta:
        model = Element
        fields = ('handbook', 'version',)


class ValidateFilter(filters.FilterSet):
    catalog = filters.CharFilter(field_name='handbook__title',
                                 lookup_expr='contains')
    code = filters.CharFilter(field_name='el_code',
                              lookup_expr='contains')
    value = filters.CharFilter(field_name='el_value',
                               lookup_expr='contains')
    date = filters.CharFilter(field_name='handbook__date',
                              lookup_expr='contains')
    version = filters.CharFilter(field_name='handbook__version',
                                 lookup_expr='contains')

    class Meta:
        model = Element
        fields = ('handbook', 'version', 'el_code', 'el_value')
