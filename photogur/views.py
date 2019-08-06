from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from photogur.models import Picture, Comment
from photogur.forms import LoginForm, Form


def root(request):
    return HttpResponseRedirect('home')


def login_view(request):
    form = LoginForm()
    context = {'form': form}
    http_response = render(request, 'login.html', context)
    return HttpResponse(http_response)


def pictures(request):
    context = {'pictures': Picture.objects.all()}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)


def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}
    response = render(request, 'picture.html', context)
    return HttpResponse(response)


def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {'pictures': search_results, 'query': query}
    return render(request, 'search.html', context)


def create_comment(request):
    picture_id = request.POST['picture']
    picture = Picture.objects.filter(id=picture_id).first()
    name = request.POST['name']
    message = request.POST['message']
    new_comment = Comment(picture=picture, name=name, message=message)
    new_comment.save()
    return HttpResponseRedirect(f'/pictures/{picture_id}')
    
