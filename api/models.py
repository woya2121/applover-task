from django.db import models




class Book(models.Model):
    serial_number = models.CharField(max_length=6)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    is_borrowed = models.BooleanField(default=False)
    # clients = models.ForeignKey(
    #     LibraryClient, on_delete=models.CASCADE, blank=True, null=True
    # )

    def __str__(self) -> str:
        return self.title

class LibraryClient(models.Model):
    card_number = models.CharField(max_length=6)
    date = models.DateTimeField(auto_now_add=True)
    books = models.ForeignKey(Book,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.card_number
