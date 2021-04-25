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
![add_book](https://user-images.githubusercontent.com/78141706/115997499-f1b03580-a600-11eb-9b1b-20fb79f5cf29.jpg)
![comments1](https://user-images.githubusercontent.com/78141706/115997503-f2e16280-a600-11eb-83b3-cfe6c013ec02.jpg)
![hp1](https://user-images.githubusercontent.com/78141706/115997504-f379f900-a600-11eb-84fd-d5ed2d47d107.jpg)
![hp2](https://user-images.githubusercontent.com/78141706/115997505-f379f900-a600-11eb-8ab7-c15df5374d6b.jpg)
![library1](https://user-images.githubusercontent.com/78141706/115997506-f4128f80-a600-11eb-8d59-2b7331bfe317.jpg)
![loginpage](https://user-images.githubusercontent.com/78141706/115997507-f4128f80-a600-11eb-9fe0-a3fca7df9dc2.jpg)
![logout](https://user-images.githubusercontent.com/78141706/115997508-f4ab2600-a600-11eb-936f-7e3ef00f3110.jpg)
![manage](https://user-images.githubusercontent.com/78141706/115997509-f4ab2600-a600-11eb-95fb-eb87d7af4b8c.jpg)
![prodV1](https://user-images.githubusercontent.com/78141706/115997511-f543bc80-a600-11eb-966e-6205400877d3.jpg)
![requests1](https://user-images.githubusercontent.com/78141706/115997512-f5dc5300-a600-11eb-8eb1-2553fff64f37.jpg)
![search_bar](https://user-images.githubusercontent.com/78141706/115997514-f5dc5300-a600-11eb-85a8-474b6bc69684.jpg)
![signup1](https://user-images.githubusercontent.com/78141706/115997516-f674e980-a600-11eb-89cb-61f2a5ac2836.jpg)



