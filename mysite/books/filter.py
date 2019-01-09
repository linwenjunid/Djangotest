import django_filters
from .models import Book


class UserFilter(django_filters.rest_framework.FilterSet):
    min_date = django_filters.DateFilter(field_name='publication_date', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='publication_date', lookup_expr='lt')

    class Meta:
        model = Book
        fields = ['min_date', 'max_date']