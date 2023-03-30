from django.db import models
from django.contrib.auth.models import AbstractUser

class Cards(models.Model):
    title = models.CharField('title', max_length=100)
    processor = models.CharField('processor', max_length=100)
    video_card = models.CharField('video_card', max_length=100)
    motherboard = models.CharField('motherboard', max_length=100)
    RAM = models.CharField('RAM', max_length=100)
    power_unit = models.CharField('power_unit', max_length=100)
    memory_storage = models.CharField('processor', max_length=100)
    body = models.CharField('body', max_length=100)
    date = models.DateTimeField('date')
    # full_descriprion = models.TextField('full_descriprion')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта сборки'
        verbose_name_plural = 'Карты сборок'

