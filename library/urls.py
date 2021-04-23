from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    ##Dashboard
    url(r'^$',views.home, name ='home'),
    url(r'^signup/$',views.signup, name='signup'),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="dashboard/login.html"), name="login"),
    url( r'^logout/$',auth_views.LogoutView.as_view(template_name="dashboard/logged_out.html"), name="logout"),
    url(r'^library/$',views.library, name ='library'),
    url(r'^add_book',views.add_book, name ='add_book'),
    path("update/<int:id>",views.update, name="update"),
    path("delete/<int:id>",views.delete, name="delete"),    
    path("library/products/<int:myid>",views.productView, name="ProductView"),
    path("library/search/",views.search, name="Search"),


    ##Rent_requests
    path("request_portal", views.request_portal, name="request_portal"),
    path("create_request/<int:id>", views.create_request, name="create_request"),
    path("reject_request/<int:id>", views.reject_request, name="reject_request"),
    path("accept_request/<int:id>", views.accept_request, name="accept_request"),
    path("delete_request/<int:id>", views.delete_request, name="delete_request"),
    

    ##BookComments
    path('postComment', views.postComment, name="postComment"),

    #BorrowedBooks
    path("deposit/<int:id>", views.deposit, name="deposit"),
    path("create_renew_request/<int:id>", views.create_renew_request, name="create_renew_request"),
        
]
        