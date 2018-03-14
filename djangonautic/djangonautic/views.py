from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("homepage")
    return render(request, 'homepage.htm')

def about(request):
    #return HttpResponse("about")
    return render(request, 'about.htm')
