from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Request, Book

class SignUpForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name','last_name','username','email')		

class AddBookForm(ModelForm):

	class Meta:
		model = Book
		fields = '__all__'
		widgets = {
			'times_borrowed':forms.TextInput(attrs={'readonly': True}),
		}

class RequestForm(ModelForm):

	class Meta:
		model = Request
		fields = ('borrower_id', 'book_id', 'Days')
		widgets = {
			'borrower_id':forms.TextInput(attrs={'readonly': True}),
			'book_id':forms.TextInput(attrs={'readonly': True}),

		}

