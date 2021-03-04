from rest_framework.routers import DefaultRouter

from books.views import (
    BookViewSet, RentedBookViewSet, ReviewViewSet, SavedBookViewSet,
)

router = DefaultRouter()
router.register(
    prefix='books', viewset=BookViewSet, basename='books',
)
router.register(
    prefix='rented_books', viewset=RentedBookViewSet, basename='rented_books',
)
router.register(
    prefix='reviews', viewset=ReviewViewSet, basename='reviews',
)
router.register(
    prefix='saved_books', viewset=SavedBookViewSet, basename='saved_books',
)
urlpatterns = router.urls
