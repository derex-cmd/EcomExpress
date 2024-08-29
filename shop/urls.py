from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopname'),
    path('product/<str:product_id>/', views.productview, name='productview'),
    path('contact/', views.contact, name='contact'),

]