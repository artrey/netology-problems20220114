from django_filters import rest_framework as filters

from demo.models import Author


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    birthdate = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Author
        fields = ['name', 'nick', 'books__title', 'birthdate']


/api/v1/authors/?name=ush&birthdate_after=1900-01-01&birthdate_before=1920-01-01
