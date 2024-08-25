from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.last_name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=90, verbose_name='Заголовок')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    year_of_creation = models.IntegerField(verbose_name='Год создания')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
