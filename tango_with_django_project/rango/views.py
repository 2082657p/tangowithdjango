from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <br/> <a href='/rango/about'>About</a>")

def about(request):
<<<<<<< HEAD
    return HttpResponse("Rango says here is the about page. \
                        <br/> <a href='/rango/'>Index</a> \
                        <br/>This tutorial was put together by Jack Parkinson, 2082657")
=======
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a> <br/>This tutorial was put together by Jack Parkinson, 2082657")
>>>>>>> 040f172e153d028673435f0b4d31af0f69fbff97
