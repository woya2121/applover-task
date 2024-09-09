from rest_framework import generics

from .models import Book, LibraryClient
from .serializers import BookSerializer, LibraryClientSerialzier


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class LibraryClientListCreate(generics.ListCreateAPIView):
    queryset = LibraryClient.objects.all()
    serializer_class = LibraryClientSerialzier
