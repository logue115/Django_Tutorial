from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return HttpResponse("Hello, Django Home!")

def time(request):
    now=datetime.now()

    html_content = "<html><head><title>Hello, Django</title></head><body>"
    html_content += "<strong>Hello Django!</strong> on" + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"

    return HttpResponse(html_content)

def time_template(request):
    now=datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "hello Django",
            'message' : "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }          
    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
            }
        )
   
# Create your views here.
