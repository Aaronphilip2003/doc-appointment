from django.urls import path
from . import views

urlpatterns=[
    path("hello/",views.say_hello),
    path('appointment/', views.appointment_form, name='appointment_form'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),  # Define the success URL
]

