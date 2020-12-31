from django.http import HttpResponse
from bs4 import BeautifulSoup

def helloworld(request):
    return HttpResponse('<h1>hello world</h1>')

def testooooo(request):
    soup = BeautifulSoup(open('sample3.html',encoding="utf-8"), 'html.parser')
    #test = '<h1><a href= "http://www.google.com/"> hello world </a></h1>'
    return HttpResponse(soup)