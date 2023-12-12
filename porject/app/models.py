from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(verbose_name='Тело статьи')
    date = models.DateTimeField(verbose_name='Дата ')
    agree = models.BooleanField(verbose_name='Опубликовано')
    url = models.URLField(verbose_name='Ссылка')
    def __str__(self):
        return f'пользователь {self.name} {self.age}'

class Posts(models.Model):
    title = models.CharField(max_length=25)
    text = models.TextField()
    is_published = models.BooleanField
    date = models.DateField()
    url = models.URLField()

    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'