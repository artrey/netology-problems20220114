from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from demo.filters import AuthorFilter
from demo.models import Author
from demo.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['name', 'nick', 'books__title']
    filterset_class = AuthorFilter
    search_fields = ['name', 'nick', 'books__title']
    ordering_fields = ['name', 'books__title']


/api/v1/authors/?name=Pushkin&books__title=Onegin&search=data&ordering=-nick
