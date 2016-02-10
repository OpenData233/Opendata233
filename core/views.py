from django.shortcuts import render, redirect
from django.views.generic import FormView
#from core.forms import SubscriptionForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, 'core/home.html', {})


def about(request):
    return render(request, 'core/about.html', {})


def candidatebio(request):
    return render(request, 'core/candidate_bio.html', {})


def mahama(request):
    return render(request, 'core/mahama.html', {})


def nana(request):
    return render(request, 'core/nana.html', {})


def greenstreet(request):
    return  render(request, 'core/greenstreet.html', {})
