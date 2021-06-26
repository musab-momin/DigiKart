
from django.contrib import admin
from django.urls import path
from shop import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('tracker', views.tracker, name="tracker"),
    path('search', views.search, name="search"),
    path('productview/<int:id>', views.productview, name="productview"),
    path('checkout', views.checkout, name="checkout"),
    path('login', views.loginUser, name="loginpage"),
    path('signup', views.registerUser, name='registerpage'),
    path('logout', views.logoutUser, name="checkout"),
    path('handlepayment', views.handlepayment, name='handlepayment')
]