# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request, 'log/index.html')

def register(request):
    errors = User.objects.register(request.POST)
    print '3'
    print errors
    if len(errors) == 0:
        request.session['id'] = User.objects.filter(email=request.POST['email'])[0].id
        request.session['name'] = request.POST['first_name']
        print '4'
        return redirect('/success')
    else:
        for error in errors:
            messages.info(request, error)
        print 'error check'
        return redirect('/')


def login(request):
    errors = User.objects.login(request.POST)

    if len(errors) == 0:
        request.session['id'] = User.objects.filter(email=request.POST['email'])[0].id
        request.session['name'] = User.objects.filter(email=request.POST['email'])[0].first_name
        return redirect('/success')
    for error in errors:
        messages.info(request, error)
    return redirect('/')

def success(request):

    return render(request, 'log/success.html')
