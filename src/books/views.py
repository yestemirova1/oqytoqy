from typing import Tuple

from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from books.models import Book, SavedBook, RentedBook, Review
from books.serializers import (
    BookSerializer, SavedBookSerializer, ReviewSerializer,
)


class BookViewSet(ModelViewSet):
    queryset: QuerySet = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ('get',)
    filter_backends: Tuple = (SearchFilter, DjangoFilterBackend)
    search_fields: Tuple = ('title', 'author')
    filterset_fields: Tuple = ('genre',)


class RentedBookViewSet(ModelViewSet):
    queryset: QuerySet = RentedBook.objects.all()
    serializer_class = BookSerializer
    http_method_names = ('get', 'post', 'patch')


class ReviewViewSet(ModelViewSet):
    queryset: QuerySet = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ('get', 'post')
    filter_backends: Tuple = (SearchFilter, DjangoFilterBackend)
    search_fields: Tuple = ('text',)
    filterset_fields: Tuple = ('book_id',)


class SavedBookViewSet(ModelViewSet):
    queryset: QuerySet = SavedBook.objects.all()
    serializer_class = SavedBookSerializer
    http_method_names = ('get', 'post', 'delete')
