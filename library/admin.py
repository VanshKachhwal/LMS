from __future__ import unicode_literals

from django.contrib import admin
from .models import Request, BookComment, Book, BorrowedBook,StarRating

admin.site.register((Book,BookComment,Request,BorrowedBook,StarRating))