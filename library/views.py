from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm
from .models import Author, Book

def root(request):
    return render(request, template_name='library/index.html')

def index(request):
    return render(request, template_name='library/index.html')

# создание объекта модели Автор
def add_author(request):
    if request.method == "GET":
        author = AuthorForm()
        context = {
            'form': author,
            'title': "Добавление автора",
        }
        return render(request, template_name='library/add_author.html', context=context)

    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author()
            author.first_name = form.cleaned_data['first_name']
            author.last_name = form.cleaned_data['last_name']
            author.patronymic = form.cleaned_data['patronymic']
            author.date_of_birth = form.cleaned_data['date_of_birth']
            author.save()

        return index(request)

# вывод списка объектов модели Автор
def author_list(request):
    authors = Author.objects.all()
    context = {
        'title': "Авторы",
        'authors': authors,
    }
    return render(request, template_name='library/authors.html', context=context)

# создание объекта модели Книга
def add_book(request):
    if request.method == "GET":
        book = BookForm()
        context = {
            'form': book,
            'title': "Добавление книги",
        }
        return render(request, template_name='library/add_book.html', context=context)

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book()
            book.author = Author.objects.get(last_name=form.cleaned_data['author'])
            book.title = form.cleaned_data['title']
            book.genre = form.cleaned_data['genre']
            book.year_of_creation = form.cleaned_data['year_of_creation']
            book.save()

            return index(request)

# вывод списка объектов модели Книга
def book_list(request):
    books = Book.objects.all()
    context = {
        'title': "Книги",
        'books': books,
    }
    return render(request, template_name='library/books.html', context=context)
