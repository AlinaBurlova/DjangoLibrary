from django.urls import path
from .views import index, add_author, author_list, add_book, book_list

app_name = 'library'
urlpatterns = [
    path('', index, name='index'),
    path('authors/add/', add_author, name='add_author'),
    path('authors/', author_list, name='author_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
]
