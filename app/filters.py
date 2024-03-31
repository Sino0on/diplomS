import django_filters
from datetime import datetime
from .models import *
from django.db.models import Q


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', method='filter_title')

    def filter_title(self, queryset, name, value):
        # print(len(queryset))
        search_term = value
        queryset = queryset.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )
        return queryset

    class Meta:
        model = Product
        ordering = ['-created_date']
        fields = ['title', 'size', 'category', 'price']
