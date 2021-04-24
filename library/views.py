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
# from django.db.models.query import QuerySet
from django.contrib.auth.models import User

#Dashboard views
def has_group(user, group_name):
	group = Group.objects.get(name = group_name)
	return True if group in user.groups.all() else False

@login_required
def home(request):
	allProds = []
	prod = Book.objects.all().order_by('-times_borrowed')
	n = len(prod)
	if n<=12:
		nSlides = n//4 +ceil((n/4) - (n//4))
		allProds.append([prod, range(1, nSlides), nSlides])
	else:
		n=12
		nSlides = n//4 +ceil((n/4) - (n//4))
		allProds.append([prod[:n], range(1, nSlides), nSlides])
	newProds = []
	prods = Book.objects.all().order_by('-date_added')
	m = len(prods)
	if m<=12:
		mSlides = m//4 +ceil((m/4) - (m//4))
		newProds.append([prods, range(1, mSlides), mSlides])
	else:
		m=12
		mSlides = m//4 +ceil((m/4) - (m//4))
		newProds.append([prods[:m], range(1, mSlides), mSlides])
	bor_books = BorrowedBook.objects.filter(user = request.user)
	boolList = []
	for bor_book in bor_books:
		if Request.objects.filter(borrower_id = request.user, book_id = bor_book.book).exists():
			boolList.append(True)
		else:
			boolList.append(False)
	context = {'bor_books':bor_books, 'boolList' :boolList, 'allProds': allProds, 'newProds': newProds}
	return render(request, 'dashboard/home.html', context)

def signup(request):
	message = None
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			users = User.objects.filter(email = form.cleaned_data['email'])
			if len(users)>=1:
				form = SignUpForm()
				message = "Email Id is already registered"
				return render(request, 'dashboard/signup.html', {'form': form, 'message':message})
			else:
				form.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username = username, password = raw_password)
				login(request, user)
				return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'dashboard/signup.html', {'form': form, 'message':message})

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
	message = None
	if not has_group(request.user, "Librarians"):
		message = "You don't have the authority to add a book!"		
	context = {'form': form, 'message':message}
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
	message = None
	if not has_group(request.user, "Librarians"):
		message = "You don't have the authority to update this book!"
	context = {'form': form, 'message':message}
	return render(request, 'library/book_form.html', context)

@login_required
def delete(request, id):
	book = Book.objects.get(id = id)
	if request.method == "POST":
		book.delete()
		return redirect('/library')
	message = None
	if not has_group(request.user, "Librarians"):
		message = "You don't have the authority to delete this book!"
	context = {'item': book, 'message':message}
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
    if query in query in item.book_title.lower() or query in item.genre.lower() or query in item.book_author.lower() or query in item.isbn :
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
	message = None
	if book.availability<=0:
		message = "Sorry, this book is out of stock!!"
	if Request.objects.filter(borrower_id = request.user, book_id = book).exists():
		message = "You have already post a request for this book!"
	if BorrowedBook.objects.filter(user = request.user, book = book).exists():
		message = "You have already borrowed one of the copies of the book!"
	context = {'form': form, 'message':message}
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
			book.times_borrowed+=1
			book.save()
			b = BorrowedBook(book = book, user = req.borrower_id, time = req.Days)
			b.save()
			req.delete()
		else:
			b = BorrowedBook.objects.get(book = book, user = req.borrower_id)
			b.time+=req.Days
			b.save()
			req.delete()
		return redirect('/request_portal')
	message = None
	if not has_group(request.user, "Librarians"):
		message = "You don't have the authority to accept requests!"
	context = {'item': req, 'message':message}
	return render(request, "Requests/ac_conf.html", context)

@login_required
def delete_request(request, id):
	req = Request.objects.get(id = id)
	if request.method == "POST":
		req.delete()
		return redirect('/request_portal')
	message = None
	if request.user != req.borrower_id:
		message = "This link is validated for the respective user only!"
	context = {'item': req, 'message':message}
	return render(request, "Requests/del_conf.html", context)

@login_required
def reject_request(request, id):
	req = Request.objects.get(id = id)
	if request.method == "POST":
		req.delete()
		return redirect('/request_portal')
	message = None
	if not has_group(request.user, "Librarians"):
		message = "You don't have the authority to reject requests, you can delete it yourself!"
	context = {'item': req, 'message':message}
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
	Request.objects.filter(borrower_id= request.user, book_id = book).delete()
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
	message = None
	if Request.objects.filter(borrower_id = request.user, book_id = book).exists():
		message = "You have already post a request for this book!"
	if request.user != bor_book.user:
		message = "Renewing requests for this borrowed book is restricted for the respective user only!"
	context = {'form': form, 'message':message}
	return render(request, "Requests/request_form.html", context)
