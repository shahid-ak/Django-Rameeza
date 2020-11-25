from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('addbook', views.addbook, name='addbook'),
    path('addcatagory', views.addcatagory, name='addcatagory'),
    path('delcatagory', views.delcatagory, name='delcatagory'),
    path('books', views.allbooks, name='allbooks'),
    path('users', views.users, name='users'),
    path('opencatagory/<int:cat_id>',views.opencatagory, name='opencatagory'),
    path('viewbook/<int:book_id>',views.viewbook, name='viewbook'),
    path('delbook/<int:book_id>',views.delbook, name='delbook'),
    path('logout', views.logout, name='logout'),
]