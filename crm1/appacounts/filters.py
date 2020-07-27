import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class Orderfilter(django_filters.FilterSet):

    start_date = DateFilter(field_name="date_created", lookup_expr='gto')
    end_date = DateFilter(field_name='date_created', lookup_expr='lto')
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = orders
        fields = '__all__'
        exclude = ['custumer', 'date_created']