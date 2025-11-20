from django.shortcuts import render
from django.http import HttpResponse
from educationalapplication.models import Registration, Contactreg
from educationalapplication.forms import ParentregForm, ContactregForm


def home_view(request):
    return render(request, 'educationalapplication/home.html/')

def about_view(request):
    return render(request, 'educationalapplication/about.html/')


def adminpage_view(request):
    data = Registration.objects.all()
    data_1 = Contactreg.objects.all()
    return render(request, 'educationalapplication/adminpage.html/', {'d' : data, 'd1' : data_1})

def classix_view(request):
    return render(request, 'educationalapplication/classix.html/')

def classviii_view(request):
    return render(request, 'educationalapplication/classviii.html/')

def classx_view(request):
    return render(request, 'educationalapplication/classx.html/')

def contactus_view(request):
    if request.method == "POST":
        form = ContactregForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your message has been sent successfully!")
    else:
        form = ContactregForm()

    return render(request, 'educationalapplication/contactus.html', {'f': form})


def latestnews_view(request):
    return render(request, 'educationalapplication/latestnews.html/')

def parentreg_view(request): 
    if request.method == "POST":
        form = ParentregForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully!")  # optional redirect
    else:
        form = ParentregForm()  # Instantiate empty form for GET request
    return render(request, 'educationalapplication/parentreg.html', {'f': form})

    return render(request, 'educationalapplication/parentreg.html', {'f': form})



def photos_view(request):
    return render(request, 'educationalapplication/photos.html/')


def vedios_view(request):
    return render(request, 'educationalapplication/vedios.html/')


