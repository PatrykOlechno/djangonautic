from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def article_list(request):
    article = Article.objects.all().order_by('-date')
    return render(request, 'articles/article_list.htm', {'articles': article})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.htm', {'article': article})

@login_required(login_url="/accounts/login")
def article_create(request):
    return render(request, 'articles/article_create.htm')
