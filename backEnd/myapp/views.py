from django.shortcuts import render
from django.http.response import HttpResponse


def Test(request):
    if request.method == "POST" :
        print(request.POST)
        username = request.POST.get("username")
        print(username)
        return HttpResponse(username)
    else :
        print(request)
