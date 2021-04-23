from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.contrib.auth.models import Group
from django.http import Http404
from .forms import SignUpForm, AddBookForm, RequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from math import ceil
import json
from .models import Request, BookComment, Book, BorrowedBook
from django.utils.timezone import now
from django.db.models.query import QuerySet

#Dashboard views
def has_group(user, group_name):
	group = Group.objects.get(name = group_name)
	return True if group in user.groups.all() else False

@login_required
def home(request):
	bor_books = BorrowedBook.objects.filter(user = request.user)
	boolList = []
	for bor_book in bor_books:
		if Request.objects.filter(borrower_id = request.user, book_id = bor_book.book).exists():
			boolList.append(True)
		else:
			boolList.append(False)
	# print(boolList)
	# print(Request.objects.all())
	context = {'bor_books':bor_books, 'boolList' :boolList}
	return render(request, 'dashboard/home.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			# user.refresh_from_db()
			# login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'dashboard/signup.html', {'form': form})


#Library views
@login_required
def library(request):
	allProds = []
	catprods = Book.objects.values('genre', 'id')
	cats = {item['genre'] for item in catprods}
	for cat in cats:
		prod = Book.objects.filter(genre = cat)
		n = len(prod)
		nSlides = n//4 +ceil((n/4) - (n//4))
		allProds.append([prod, range(1, nSlides), nSlides])
	params = {'allProds': allProds}
	return render(request, 'library/library.html', params)

@login_required
def add_book(request):
	form = AddBookForm()
	if request.method == 'POST':
		form = AddBookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/library')
	context = {'form': form}
	return render(request, 'library/book_form.html', context)

@login_required
def update(request, id):
	book = Book.objects.get(id = id)
	form = AddBookForm(instance = book)
	if request.method == 'POST':
		form = AddBookForm(request.POST, instance = book)
		if form.is_valid():
			form.save()
			return redirect('/library')
	context = {'form': form}
	return render(request, 'library/book_form.html', context)

@login_required
def delete(request, id):
	book = Book.objects.get(id = id)
	if request.method == "POST":
		book.delete()
		return redirect('/library')
	context = {'item': book}
	return render(request, 'library/delete.html', context)

@login_required
def productView(request, myid):
	product = Book.objects.filter(id=myid)
	comments = BookComment.objects.filter(book = product[0], parent= None)
	replies = BookComment.objects.filter(book =product[0]).exclude(parent = None)
	replyDict = {}
	if Request.objects.filter(borrower_id = request.user, book_id = product[0]).exists():
		already_sent = True
	else:
		already_sent = False
	if BorrowedBook.objects.filter(user = request.user, book = product[0]).exists():
		already_bor = True
	else:
		already_bor = False
	print(Request.objects.filter(borrower_id = request.user, book_id = product[0]), BorrowedBook.objects.filter(user = request.user, book = product[0]))
	for reply in replies:
		if reply.parent.sno not in replyDict.keys():
			replyDict[reply.parent.sno] = [reply]
		else:
			replyDict[reply.parent.sno].append(reply)
	context = {'product':product[0], 'comments':comments, 'replyDict': replyDict, 'already_sent':already_sent, 'already_bor':already_bor}
	return render(request, 'library/prodView.html', context)

def searchMatch(query, item):
    if query in item.summary.lower() or query in item.book_title.lower() or query in item.genre.lower() or query in item.book_author.lower() or query in item.isbn :
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Book.objects.values('genre', 'id')
    cats = {item['genre'] for item in catprods}
    for cat in cats:
        prodtemp = Book.objects.filter(genre=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'library/search.html', params)


#Requests views
@login_required
def create_request(request, id):
	book = Book.objects.get(id = id)
	form = RequestForm(initial={'borrower_id': request.user, 'book_id':book, 'renew':False})
	if request.method == 'POST':
		form = RequestForm(request.POST, request.FILES or None)
		print(form.errors)
		if form.is_valid():
			form.save()
			return redirect('/library')
	context = {'form': form}
	return render(request, "Requests/request_form.html", context)

@login_required
def request_portal(request):
	if has_group(request.user, "Librarians"):
		rent_requests = Request.objects.filter(renew = False)
		renew_requests = Request.objects.filter(renew = True)
	else:
		rent_requests = Request.objects.filter(borrower_id = request.user, renew = False)
		renew_requests = Request.objects.filter(borrower_id = request.user, renew = True)
	params = {'rent_requests': rent_requests, 'renew_requests': renew_requests}
	return render(request, "Requests/request_portal.html", params)

@login_required
def accept_request(request, id):
	req = Request.objects.get(id = id)
	book = req.book_id
	if request.method == "POST":
		if req.renew == False:
			book.rent()
			b = BorrowedBook(book = book, user = req.borrower_id, time = req.Days)
			b.save()
			req.delete()
		else:
			b = BorrowedBook.objects.get(book = book, user = req.borrower_id)
			b.time+=req.Days
			b.save()
			req.delete()
		return redirect('/request_portal')
	context = {'item': req}
	return render(request, "Requests/ac_conf.html", context)

@login_required
def delete_request(request, id):
	req = Request.objects.get(id = id)
	if request.method == "POST":
		req.delete()
		return redirect('/request_portal')
	context = {'item': req}
	return render(request, "Requests/del_conf.html", context)

@login_required
def reject_request(request, id):
	req = Request.objects.get(id = id)
	if request.method == "POST":
		req.delete()
		return redirect('/request_portal')
	context = {'item': req}
	return render(request, "Requests/rj_conf.html", context)


##BookComments
def postComment(request):
	if request.method == "POST":
		comment = request.POST.get('comment')
		user = request.user
		bookSno = request.POST.get('id')
		book = Book.objects.get(id = bookSno)
		parentSno = request.POST.get('parentSno')
		if parentSno == "":
			comment = BookComment(comment = comment, user = user, book = book)
			comment.save()
		else:
			parent = BookComment.objects.get(sno = parentSno)
			comment = BookComment(comment = comment, user = user, book = book, parent = parent)
			comment.save()
	
	return redirect(f'/lms/library/products/{book.id}')

##Borrowed Books
def deposit(request, id):
	bor_book = BorrowedBook.objects.get(id = id)
	book = bor_book.book
	book.availability+=1
	book.save()
	bor_book.delete()
	return redirect('/')

@login_required
def create_renew_request(request, id):
	bor_book = BorrowedBook.objects.get(id = id)
	book = bor_book.book
	form = RequestForm(initial={'borrower_id': bor_book.user, 'book_id':book})
	if request.method == 'POST':
		form = RequestForm(request.POST, request.FILES or None)
		# print(form.errors)
		if form.is_valid():
			form.save()
			req = Request.objects.get(borrower_id= request.user, book_id = book)
			req.renew = True
			req.save()
			print(req)
			return redirect('/')
	context = {'form': form}
	return render(request, "Requests/request_form.html", context)