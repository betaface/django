# I have created this file - Andy
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Anish', 'place':'S Town'}
    return render(request, 'index.html', params)
    # return HttpResponse("Home") 

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremover(request):
    return HttpResponse("spaceremover")

def charcount(request):
    return HttpResponse("charcount")
 