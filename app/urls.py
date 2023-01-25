from django.urls import path
from . import views


urlpatterns = [
    path('', views.front, name='front'),
    path('/home', views.home, name='home'),
    path('/ho', views.ho, name='ho'),
    path('form/', views.form, name='form'),
    path('add/', views.receipt_data),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
     path('add_receipt/', views.add_receipt, name='add_receipt'),
   
   

    path('pdf/<int:bill_to>/', views.pdf, name='pdf'),
    path('soft/', views.soft, name='soft'),
    path('hard/', views.hard, name='hard'),
    path('receipt/<int:received_from>/', views.receipt, name='receipt'),
  
    
    
   
    
    
]