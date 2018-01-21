from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    context = {'msg' : 'homepage'}
    return render(request, 'home_page.html', context=context)


def about_page(request):
    context = {'msg' : 'aboutpage'}
    return render(request, 'home_page.html', context=context)


def contact_page(request):
    contact_form = ContactForm()
    context = {
        'title' : 'Welcome to Contact Us Page!',
        'form' : contact_form
    }
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, 'contact/view.html', context=context)