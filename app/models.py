from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Shop(AbstractUser):
    shop_name = models.CharField(max_length=123, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_shop = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to='avatars/%Y/%m/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    images = models.ManyToManyField('ShopImage')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class ShopImage(models.Model):
    image = models.ImageField(upload_to='shop/images/')


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PriceHistory(models.Model):
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.price} - {self.created_at}'

    class Meta:
        verbose_name = 'История цены'
        verbose_name_plural = 'Истории цены'


class Product(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    price = models.ForeignKey(PriceHistory, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, related_name='products')
    size = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, blank=True)
    quantity = models.PositiveIntegerField(blank=True, default=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProdImgs(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='images')
    images = models.ImageField(upload_to='images/%Y/%m/')

    def __str__(self):
        return f'{self.product.title} - {self.pk}'

    class Meta:
        verbose_name = 'Фотка продукта'
        verbose_name_plural = 'Фотки продуктов'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    price = models.ForeignKey(PriceHistory, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} - {self.pk}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

