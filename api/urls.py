from django.urls import path

from . import views


urlpatterns = [
    path("book/", views.BookListCreate.as_view(), name="book-view-create"),
    path(
        "book/<int:pk>/",
        views.BookRetrieveUpdateDelete.as_view(),
        name="book-view-update",
    ),
    path(
        "client/", views.LibraryClientListCreate.as_view(), name="library-client-create"
    ),
]
