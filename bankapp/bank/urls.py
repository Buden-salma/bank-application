from django.urls import path
from bank import views

urlpatterns=[
    path('',views.homepage,name='home'),
    path('login/',views.loginview,name='login'),
    path('register/',views.registerview, name='register'),
    path('viewbalance/',views.View_balance,name='viewBalance'),
    path('history/',views.historypage,name='history'),
    path('transfer/',views.Transfer,name='transfer'),
    path('logout/',views.logoutview,name='logout'),
     path('delete/<int:rid>/', views.deleteView, name='delete'),
]