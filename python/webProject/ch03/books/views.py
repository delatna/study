#file name : ch03/books/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest
from django.core.urlresolvers import reverse
from books.models import Book, Author, Publisher
from django.views import generic

# index
class BooksModelView(generic.TemplateView):
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super(BooksModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Book', 'Author', 'Publisher']
        return context

# List
class BookList(generic.ListView):
    model = Book

class AuthorList(generic.ListView):
    model = Author

class PublisherList(generic.ListView):
    model = Publisher

# Detail View
class BookDetail(generic.DetailView):
    model = Book

class AuthorDetail(generic.DetailView):
    model = Author

class PublisherDetail(generic.DetailView):
    model = Publisher

# Create your views here.
