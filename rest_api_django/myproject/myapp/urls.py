from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Handles GET and POST for /books/
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),  # Handles GET, PUT, DELETE for /books/<id>/
]
