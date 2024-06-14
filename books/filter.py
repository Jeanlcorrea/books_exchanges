from django_filters import FilterSet, CharFilter, DateFilter, BooleanFilter

from books.models import BookModels

class ListBooksFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='startswith')
    title = CharFilter(field_name='title', lookup_expr='exact')
    author = CharFilter(field_name='author', lookup_expr='exact')
    published_date = DateFilter(field_name='published_date', lookup_expr='iexact')
    genre = CharFilter(field_name='genre', lookup_expr='startswith')
    is_available_for_exchange = BooleanFilter(field_name='is_available_for_exchange')

    class Meta:
        model = BookModels
        fields = ['id', 'title', 'author', 'published_date', 'genre', 'is_available_for_exchange']
