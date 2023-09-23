import django_filters
from .models import Property

class ProppertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ['name', 'place', 'description','category']