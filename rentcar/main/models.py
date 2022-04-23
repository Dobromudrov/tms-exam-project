from django.db import models
from django.urls import reverse
from django.conf import settings


class CarsTable(models.Model):
    title = models.CharField(max_length=100, verbose_name='Модель Машины')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/cars', verbose_name='Фото')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена | BYN', null=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')
    time_update = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Статус Публикации')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Машину'
        # единственное число
        verbose_name_plural = 'Машины'
        # множественное число


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория Машин'
        # единственное число
        verbose_name_plural = 'Категория Машин'
        # множественное число


class OrderTable(models.Model):
    # choice = models.ForeignKey('post', on_delete=models.PROTECT, null=True, verbose_name='Выбор')
    choice = models.ForeignKey('CarsTable', on_delete=models.PROTECT, null=True, verbose_name='Машина')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    comment = models.TextField(max_length=100, verbose_name='Комментарий')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    time_create = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Заявка клиента'
        # единственное число
        verbose_name_plural = 'Заявки клиентов'
        # множественное число
        ordering = ['-time_create', 'choice']


class FeedbackTable(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Email')
    comment = models.TextField(max_length=100, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Обратная связь'
        # единственное число
        verbose_name_plural = 'Обратная связь'
        # множественное число
