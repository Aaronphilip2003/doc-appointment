from django.shortcuts import render,redirect
from django.http import HttpResponse
from pymongo import MongoClient

# Create your views here.

def say_hello(request):
    return render(request,"hello.html")

def appointment_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        appointment_time = request.POST.get('appointment_time')

        # MongoDB Atlas connection URI
        uri = "mongodb+srv://aaronphilip2003:Aaron123@cluster0.lk2el6b.mongodb.net/?retryWrites=true&w=majority"

        # Create a new client and connect to the server
        client = MongoClient(uri)

        # Access a specific database and collection
        db = client['docApp']
        appointments_collection = db['appointments']

        # Create a document to insert
        appointment_doc = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'appointment_time': appointment_time
        }

        # Insert the document
        appointments_collection.insert_one(appointment_doc)

        return render(request, 'appointment_success.html')

    return render(request, 'appointmentForm.html')

def appointment_success(request):
    return render(request, 'appointment_success.html')
