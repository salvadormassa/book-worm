from django.db import models


class LowerCaseField(models.CharField):
    """ Set in place of CharField, converts to lowercase """

    def get_prep_value(self, value):
        return str(value).lower()

class TruncatingCharField(models.CharField):
    def get_prep_value(self, value):
        value = super(TruncatingCharField, self).get_prep_value(value)
        if value:
            return value[:self.max_length]
        return value

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Format(models.Model):
    type = models.CharField(max_length=50, unique=True)

class Condition(models.Model):
    LIKE_NEW = 'LN'
    FINE = 'F'
    NEAR_FINE = 'NF'
    VERY_GOOD = 'VG'
    GOOD = 'G'
    FAIR = 'F'
    POOR = 'P'
    BOOK_CONDITIONS = [
        (LIKE_NEW, 'Like New'),
        (FINE, 'Fine'),
        (NEAR_FINE, 'Near Fine'),
        (VERY_GOOD, 'Very Good'),
        (GOOD, 'Good'),
        (FAIR, 'Fair'),
        (POOR, 'Poor'),
    ]
    condition = models.CharField(max_length=2, choices=BOOK_CONDITIONS)
    description = models.TextField()
    price_modifier = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, blank=True)

class Book(models.Model):
    HARD_COVER = 'HC'
    SOFT_COVER = 'SC'
    OTHER = 'OT'
    COVERS = [
        (HARD_COVER, 'Hard Cover'),
        (SOFT_COVER, 'Soft Cover'),
        (OTHER, 'Other'),
    ]
    isbn = models.CharField(max_length=13, primary_key=True)  # Books < 2007 have 10 digit, <= 2007 have 13 digits
    title = TruncatingCharField(max_length=250)  # CharField max length is 255
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='/thumbnails')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    page_count = models.PositiveIntegerField()
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    dust_jacket = models.BooleanField()
    msrp = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=True)

class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    dust_jacket = models.BooleanField()
    base_price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
