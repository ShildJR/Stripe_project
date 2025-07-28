from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=80, verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание')
    # цена указана в копейках
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    # Перевод в рубли
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']