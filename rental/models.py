from django.db import models

class Bike(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price_per_hour = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Цена за час"
    )
    available = models.BooleanField(default=True, verbose_name="Доступен")

    def __str__(self):
        return self.name
