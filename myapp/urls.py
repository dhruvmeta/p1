from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('project/',views.project),
   path('testimonial/',views.testimonial),
   path('contact/',views.contact),
  
]