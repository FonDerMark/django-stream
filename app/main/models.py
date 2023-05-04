from django.db import models

class GenreRu(models.Model):
    GENRE_CHOICES_RU = [
        ('Боевик', 'Боевик'),
        ('Приключения', 'Приключения'),
        ('Аниме', 'Аниме'),
        ('Биография', 'Биография'),
        ('Комедия', 'Комедия'),
        ('Криминал', 'Криминал'),
        ('Детектив', 'Детектив'),
        ('Документальный', 'Документальный'),
        ('Драма', 'Драма'),
        ('Семейный', 'Семейный'),
        ('Фантастика', 'Фантастика'),
        ('Исторический', 'Исторический'),
        ('Исторический боевик', 'Исторический боевик'),
        ('Ужасы', 'Ужасы'),
        ('Мюзикл', 'Мюзикл'),
        ('Триллер', 'Триллер'),
        ('Мистика', 'Мистика'),
        ('Нуар', 'Нуар'),
        ('Романтика', 'Романтика'),
        ('Научная фантастика', 'Научная фантастика'),
        ('Научно-фантастический боевик', 'Научно-фантастический боевик'),
        ('Спорт', 'Спорт'),
    ]
    GENRE_CHOICES_EN = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Anime', 'Anime'),
        ('Biography', 'Biography'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Detective', 'Detective'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Historical', 'Historical'),
        ('Historical action', 'Historical action'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Mystic', 'Mystic'),
        ('Noir', 'Noir'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Sci-fi action', 'Sci-fi action'),
        ('Sport', 'Sport'),
        ('Thriller', 'Thriller'),
    ]
    name_ru = models.CharField(max_length=20, choices=GENRE_CHOICES_RU)
    name_en = models.CharField(max_length=20, choices=GENRE_CHOICES_EN)

    def __str__(self):
        return self.name_en


# Create your models here.
class Film(models.Model):
    title_ru = models.CharField(max_length=30)
    title_en = models.CharField(max_length=30)
    year = models.IntegerField(
        min_value=1900,
        max_value=2021
    )
    file_max = models.FileField(upload_to='films/')
    poster = models.ImageField(upload_to='posters/')
    description = models.CharField(max_length=500)
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    actors = models.CharField(max_length=100)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'film'
        verbose_name_plural = 'films'

