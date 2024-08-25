from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'patronymic', 'date_of_birth']
        widgets = {'date_of_birth': forms.DateInput(format=('%m/%d/%Y'),
                                                    attrs={'type': 'date'})}

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'genre', 'year_of_creation']
