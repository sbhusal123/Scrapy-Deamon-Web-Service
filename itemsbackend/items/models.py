from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=250, unique=True)
    price = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
