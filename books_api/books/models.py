from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    publisher = models.CharField(max_length=200, blank=False, default='')
    author = models.CharField(max_length=200, blank=False, default='')
    year = models.IntegerField(blank=False)

    def __str__(self):
        return {
            "title": self.title,
            "description": self.description,
            "publisher": self.publisher,
            "author": self.author,
            "year": self.year
        }.__str__()



