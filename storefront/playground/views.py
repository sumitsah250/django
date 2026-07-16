from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request ->response 
# request handler
# action 

def say_hello(request):
    x=12
    y=13
    return render(request, "hellow.html")




def say_no(request):
    number = 12
    if(number>10):
        return HttpResponse("Yes")
    else:
        return HttpResponse("No")
