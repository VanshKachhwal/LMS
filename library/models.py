from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

class Book(models.Model):
    book_pk = models.AutoField
    book_title = models.CharField(max_length=50, default = "")
    book_author = models.CharField(max_length=50, default = "")
    book_publisher = models.CharField(max_length=50, default = "")
    genre = models.CharField(max_length=50, default="")
    availability = models.IntegerField(default=0)
    times_borrowed = models.IntegerField(default =0)
    summary = models.CharField(max_length=300)
    isbn = models.CharField(max_length = 30)
    image = models.ImageField(upload_to='images', default="")
    date_added = models.DateTimeField(default = now,editable = False)

    def __str__(self):
        return self.book_title

    def rent(self):
        self.availability-=1
        self.save()

class Request(models.Model):
    borrower_id = models.ForeignKey(User, on_delete = models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete = models.CASCADE)
    Days = models.IntegerField()
    renew = models.BooleanField(default = False)

    def __str__(self):
        return self.borrower_id.username + "--"  + self.book_id.book_title + "--" +   str(self.Days)

class BookComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fine = models.IntegerField(default = 0)
    accepted = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()
