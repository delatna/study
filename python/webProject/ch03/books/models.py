# file name : ch03/books/models.py

from django.db import models

# Create your models here.

## id, title, authors, publisher, publication_data
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

##출판사 : 이름, 주소, 웹사이트
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name
    
