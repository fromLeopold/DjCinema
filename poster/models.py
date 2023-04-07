from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class FilmGenre(models.Model):
    genre = models.CharField(primary_key=True, db_index=True,
                             max_length=50, verbose_name="Жанры")

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = "Жанры фильмов"
        verbose_name_plural = "Жанры фильмов"


class FilmProduction(models.Model):
    production = models.CharField(primary_key=True, db_index=True, max_length=50, verbose_name="Страны-производители")

    def __str__(self):
        return self.production

    class Meta:
        verbose_name = "Страны-производители фильмов"
        verbose_name_plural = "Страны-производители фильмов"


class Film(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название фильма')
    production = models.ForeignKey("FilmProduction", on_delete=models.PROTECT, verbose_name='Страна-производитель')
    year = models.PositiveSmallIntegerField(verbose_name='Год')
    genre = models.ForeignKey("FilmGenre", on_delete=models.PROTECT, verbose_name='Жанр')
    photo = models.ImageField(upload_to='photo/films/%Y/%m')
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('film', kwargs={"film_id": self.name})

    class Meta:
        verbose_name = "Фильмы"
        verbose_name_plural = "Фильмы"


class SeatCategory(models.Model):
    category = models.CharField(primary_key=True, db_index=True, max_length=50, verbose_name="Категории мест")
    description = models.TextField(null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категории мест"
        verbose_name_plural = "Категории мест"


class Session(models.Model):
    data_time = models.DateTimeField(verbose_name="Дата", null=True)
    hall_id = models.ForeignKey("Hall", on_delete=models.PROTECT)
    film_id = models.ForeignKey("Film", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.data_time)

    class Meta:
        verbose_name = "Сеансы"
        verbose_name_plural = "Сеансы"


class Price(models.Model):
    category = models.ForeignKey("SeatCategory", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = "Цены"
        verbose_name_plural = "Цены"


class SeatRow(models.Model):
    hall_id = models.ForeignKey("Hall", on_delete=models.PROTECT)
    row = models.PositiveSmallIntegerField(verbose_name='Ряд')
    place = models.PositiveSmallIntegerField(verbose_name='Место')
    category = models.ForeignKey("SeatCategory", on_delete=models.PROTECT, verbose_name='Категория мест')

    class Meta:
        verbose_name = "Места и ряды"
        verbose_name_plural = "Места и ряды"


class Hall(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    cinema_id = models.ForeignKey("Cinema", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Залы"
        verbose_name_plural = "Залы"


class Cinema(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Название")
    district = models.CharField(max_length=50, verbose_name="Район")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    numbers = models.PositiveSmallIntegerField(verbose_name="Телефон для связи")

    def get_absolute_url(self):
        return reverse('cinema', kwargs={"cinema_id": self.name})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кинотеатры"
        verbose_name_plural = "Кинотеатры"


class News(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Заголовок")
    photo = models.ImageField(upload_to='photo/news/%Y/%m')
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('new', kwargs={"new_id": self.title})

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Review(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    comment = models.TextField()

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"

