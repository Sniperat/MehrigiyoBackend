from .models import Medicine
import django_filters


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Medicine
        fields = ['name', 'title', 'weight', 'cost', 'created_at']
