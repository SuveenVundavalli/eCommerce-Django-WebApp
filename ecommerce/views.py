from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'msg': 'homepage'
    }
    if request.user.is_authenticated:
        context['premium_content'] = 'YEAHHHHH'
    return render(request, 'home_page.html', context=context)


def about_page(request):
    context = {'msg': 'aboutpage'}
    return render(request, 'home_page.html', context=context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Welcome to Contact Us Page!',
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact/view.html', context=context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'form': login_form
    }
    print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        user = authenticate(request, username=login_form.cleaned_data.get('username'),
                            password=login_form.cleaned_data.get('password'))
        if user is not None:
            login(request, user)
            context['login'] = LoginForm()
            # Redirect to success page
            return redirect('/')
        else:
            # Invalid details
            print('Error')
    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        'form': register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        print(user)
        return redirect('/')
    else:
        # Invalid register
        print('Error')
    return render(request, 'auth/register.html', context)
