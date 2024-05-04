from django.shortcuts import render, redirect
from .models import Subscriber  # Assuming you have a Subscriber model


def home(request):
    return render(request, 'myproject/home.html')

def success_page(request):
    return render(request, 'success_page.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscriber.objects.create(email=email)  # Saving the email to your database
        return redirect('success_page')  # Redirect to a success page or wherever you prefer
    return render(request, 'home.html')  # Display the form again if not a POST request

