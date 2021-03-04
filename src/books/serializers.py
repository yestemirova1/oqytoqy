from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title', 'description', 'author', 'genre', 'rating', 'image',
            'created', 'release_date', 'isbn', 'quantity', 'language',
        )


class SavedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book', 'user', 'created')


class RentedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book', 'user', 'created', 'state')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book', 'user', 'created', 'text', 'rating')
