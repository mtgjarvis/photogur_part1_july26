from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from photogur.models import Picture, Comment

def root(request):
    return HttpResponseRedirect('home')

def pictures(request):
    context = {'pictures': Picture.objects.all()}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)