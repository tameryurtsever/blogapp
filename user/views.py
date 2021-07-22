from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

import user

# Create your views here.

def register(request):
    form = forms.RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Kullanıcı kaydınız başarıyla yapılmıştır...")
            
        return redirect("index")

    context = {
        "form" : form
    }
    return render(request,"register.html",context)

def loginUser(request):
    form = forms.LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user =  authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "login.html", context)

        messages.success(request, "Hoş Geldiniz, {}".format(username))
        login(request, user)
        return redirect("index")

    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yapılmıştır...")
    return redirect("index") 
