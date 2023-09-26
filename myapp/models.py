from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, default="Нет описания")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    # Другие поля по вашему выбору

    def __str__(self):
        return self.name
