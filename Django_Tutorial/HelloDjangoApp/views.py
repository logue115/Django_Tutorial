from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
##import random

def index(request):
    now=datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "Hello Django",
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
def algorithms(request):
    return render(
        request,
        "HelloDjangoApp/algorithms.html",
        {
            'title' : "algorithms",
            
            }
        )

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(
        request,
        "HelloDjangoApp/upload.html",
        {
            'title' : "Upload",
            'content' : "Upload testing page."
            }
        )
   
# Create your views here.
"""

array1=[]
def Array_Gen():
    start=9
    stop=99
    limit=10
    array1=[random.randint(start, stop) for iter in range(limit)]
    print(array1)
        
Array_Gen()
"""