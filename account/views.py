from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserAuthenticationForm
from django.contrib.auth import login, authenticate, logout
from districts.models import District

# Create your views here.


def user_register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already registered")
    context = {}

    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['reg_form'] = form
    context['districts'] = District.objects.all()
    return render(request, 'reg_form.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request, *args, **kargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserAuthenticationForm
    context['login_form'] = form
    return render(request, 'login.html', context)


def agency_register_view(request, *args, **kwargs):
    user = request.user
    if not user.is_authenticated or not user.is_admin:
        return HttpResponse("You are not allowed to view this page")
    context = {}

    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_agency = True
            instance.save()
            return redirect('home')
        else:
            context['agency_reg_form'] = form

    return render(request, 'agency_reg_form.html', context)