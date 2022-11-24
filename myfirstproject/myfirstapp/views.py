from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)  

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydictionary)  

def myfirstpage(request):
    return render(request, "index.html")

def mysecondpage(request):
    return render(request, "sample.html")

def mythirdpage(request):
    var = "hello world"
    greeting = "hey, how are you?"
    fruits = ["apple", "mango", "banana"]
    num1, num2 = 5, 3
    ans = num1 > num2
    mydictionary = {
        "var": var,
        "msg": greeting,
        "myfruits": fruits,
        "num1": num1,
        "num2": num2,
        "ans": ans
    }
    return render(request, "sample1.html",context=mydictionary) 

def myimgpage(request, imgname):
    myimgname = str(imgname)
    myimgname = myimgname.lower()
    print(myimgname)
    if myimgname == "django":
        var =True
    elif myimgname == "python":
        var = False
    mydictionary = {
        "var": var
    }

    return render(request, "imgpage.html", context=mydictionary)

def myform(request): 
    return render(request, "myform.html")

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)