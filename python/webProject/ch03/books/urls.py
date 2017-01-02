#file name : books/urls.py

from django.conf.urls import url
from . import views

app_name = "books"
#URLconf 코딩 한다. - 정규식을 이용
urlpatterns = [
    # 127.0.0.1:8888/books/ , index.html
    url(r'^$', views.BooksModelView.as_view(), name='index'),

    # 127.0.0.1:8888/books/book/

    url(r'^book/$', views.BookList.as_view(), name='book_list'),
    url(r'^author/$', views.AuthorList.as_view(), name='author_list'),
    url(r'^publisher/$', views.PublisherList.as_view(), name='publisher_list'),

    url(r'^book/(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book_detail'),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
    url(r'^publisher/(?P<pk>\d+)/$', views.PublisherDetail.as_view(), name='publisher_detail'),
]
