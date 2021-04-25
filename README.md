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
20. Live carousels, dynamic request system, comments and reply
21. Average Star Rating system in which each user can give star rating at most 1 time to each book in the library.
<br> 

# Setting up:
As the project is based upon django which primarialy is based upon python, you need to have python installed on your device
## Clone this repository on your device
Clone the repository on your device. 

## Install django and other required modules
In the cmd enter 
<br>
``` pip install django```
<br> 
``` pip install social-auth-app-django```
<br>
``` pip install pillow```

## Migrations and running server
Navigate to the same directory as manage.py and in the command line type the following commands
<br>
```python manage.py makemigrations```
<br>
```python manage.py migrate```
<br>
```python manage.py runserver```

## Ready to go
The development server is finally up. Open chrome/firefox and in search bar type
<br>
```  localhost:8000/ ```

## Caution:
If you are accessing multiple users account from same chrome window you are directly going to login to account of previous user due to the same reason that if you once login to google from same chrome window, if you again search facebook you are already logged in, hence to access multiple users, use multiple chrome windows.

Remember to access through localhost and not 127.0.0.1 as facebook signin may have some validation issues with it!
<br>
As Kanye west said -
<br>
```  We live in future so present is our past:) ```

## Accessing users and dummy data
1. SuperUser/admin
    - Username: admin
    - Password: admin
1. Librarian
    - Username: lib1
    - Password: lib1
1. Users
    | Username | Password |
    |---|---|
    | user1 | user1 |
    | user2 | user2 | 
    | user3 | user3 | 
    | user4 | user4 |
    | user5 | user5 |


# Screenshots:
![add_book](https://user-images.githubusercontent.com/78141706/115997741-ec9fb600-a601-11eb-9840-8cd1a42e5bd6.jpg)
![hp1](https://user-images.githubusercontent.com/78141706/115997743-ee697980-a601-11eb-87c5-2070d860b607.jpg)
![hp2](https://user-images.githubusercontent.com/78141706/115997744-ee697980-a601-11eb-80bd-e865de40730c.jpg)
![library1](https://user-images.githubusercontent.com/78141706/115997745-ef021000-a601-11eb-878e-b13ebf7acfe3.jpg)
![loginpage](https://user-images.githubusercontent.com/78141706/115997746-ef9aa680-a601-11eb-878d-626c4d5ee852.jpg)
![logout](https://user-images.githubusercontent.com/78141706/115997747-ef9aa680-a601-11eb-9ec9-1d89659355e3.jpg)
![libView](https://user-images.githubusercontent.com/78141706/116003769-08648580-a61d-11eb-8e63-1ffa0cc3088d.jpg)
![requests1](https://user-images.githubusercontent.com/78141706/115997751-f0cbd380-a601-11eb-889a-ec33b89e0f67.jpg)
![search_bar](https://user-images.githubusercontent.com/78141706/115997753-f0cbd380-a601-11eb-965c-4489fcdefbc9.jpg)
![signup1](https://user-images.githubusercontent.com/78141706/115997755-f1646a00-a601-11eb-947d-378a5f0bdf28.jpg)
![starRating1](https://user-images.githubusercontent.com/78141706/116003624-5e84f900-a61c-11eb-8a60-3d12bcfd5457.jpg)
![starRating2](https://user-images.githubusercontent.com/78141706/116003626-5fb62600-a61c-11eb-8d7c-0b4d28702d9d.jpg)
![starRating3](https://user-images.githubusercontent.com/78141706/116003648-78bed700-a61c-11eb-89a6-8d01ae7c8cf2.jpg)



