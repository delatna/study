#file name : ch03/books/admin.py
from django.contrib import admin

# Register your models here.
#admin 페이지에서의 동작을 등록

from books.models import Book, Author, Publisher 

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
