from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=56)
    price = models.DecimalField(max_digits=6, decimal_places=3,blank=True, null=True)
    descriptions = models.TextField(max_length=256)
    raiting = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
