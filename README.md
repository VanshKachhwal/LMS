# LMS
Library management Web Application
<br>
# Specifications:
1. Login/Register with facebook, google, github or site registration.
2. User cannot make multiple accounts with the same email Id.
3. There are 3 kinds of accounts, librarian, user and admin, admin being the django-administrator.
4. Admin can assign or revoke roles of librarian by adding or removing users from the Librarians group.
5. Librarians have access to add or update the library database.
6. Quick searching of any book is available where user can search by book's author, genre and title.
7. A user can request to borrow a book for any no. of days by going to the respective book page in the library.
8. There is a separate page for requests where users can see their active requests/renew requests and librarians can choose to accept or reject them.
9. Librarians can update the database by going to respective book page in the library.
10. The updation system is automated, the changes in book availability are automated on account of deposits/requests getting accepted.
11. User can request to renew the period of book they have.
12. Registered users have a profile page where they they can monitor their borrowed books(deposit timer and renew deposit options).
13. There is a comments/review section in respective book page.
14. In the front page carousels are available showing the most popular books and newest arrivals in lms.
15. Requests of various users get queued in the request tab.
16. Admin and librarians can remove offensive comments by accessing the django-administrator page.
17. Books are categorized according to genres in library/similar books.
18. Checks for username not taken and email id not taken.
19. Touch of appealing frontend with carousels, managed comments and what not!
<br> 

# Setting up:
As the project is based upon django which primarialy is based upon python, you need to have python installed on your device
## Clone this repository on your device
Clone the repository on your device. 

## Install django and other required modules
In the cmd enter 
``` pip install django``` 
``` pip install social-auth-app-django```

## Migrations and running server
Navigate to the same directory as manage.py and in the command line type the following commands
```python manage.py makemigrations```
```python manage.py migrate```
```python manage.py runserver```

## Ready to go
The development server is finally up. Open chrome/firefox and in search bar type
```  localhost:8000/ ```

Remember to access through localhost and not 127.0.0.1 as facebook signin may have some validation issues with it! As Kanye west said:
```  We live in future so present is our past:) ```

#Screenshots:



