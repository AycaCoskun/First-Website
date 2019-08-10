from django.contrib import admin
from django.urls import path
from .views import (
	show_index, 
	show_contact, 
	show_about
)

urlpatterns = [
  
    path('about-us', show_about, name='about'),
    path('contact-us', show_contact, name='contact' )

]
