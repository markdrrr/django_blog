from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=56)
    price = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    descriptions = models.TextField(max_length=256)
    raiting = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='product_images/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return f'{self.product}'
