import django_filters
from django_filters import DateFilter
from .models import Destination

class OrderFilter(django_filters.FilterSet):
    startPrice = DateFilter(field_name='price', lookup_expr='gte')
    endPrice = DateFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = Destination
        fields = ['destination','off']

