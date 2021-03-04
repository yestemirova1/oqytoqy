from django.contrib import admin

from books.models import Book, Review, RentedBook, SavedBook

admin.site.register(Book)
admin.site.register(RentedBook)
admin.site.register(Review)
admin.site.register(SavedBook)
