from rest_framework import serializers

from .models import Book, LibraryClient


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["serial_number", "title", "author", "is_borrowed"]


class LibraryClientSerialzier(serializers.ModelSerializer):
    class Meta:
        model = LibraryClient
        fields = ["card_number", "date", "books"]
