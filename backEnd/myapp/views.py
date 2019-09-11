from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from myapp import models
from django.db.models import Q
import json
from datetime import date,datetime

def Test(request):
    if request.method == "POST" :
        print(request.POST)
        username = request.POST.get("username")
        print(username)
        return HttpResponse(username)
    else :
        print(request)

# class DataEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, date):
#             return obj.strftime("%Y-%m-%d")
#         else:
#             return json.JSONEncoder.default(self, obj)
def textVue(request):
    if request.method == "POST":
        pageCurrent = request.POST.get("pageCurrent")
        pageSize = request.POST.get("pageSize")
        if pageCurrent is None or (not any(pageCurrent)):
            pageCurrent = 1
        #print(not any(pageSize))
        if pageSize is None or (not any(pageSize)):
            pageSize = 10
        else:
            pageSize = int(pageSize)
        ret = models.textvue.objects.all().values().order_by("id")
        result = {}
        paginator = Paginator(ret, pageSize)
        result['dataCount'] = paginator.count
        try:
            geciList = paginator.page(pageCurrent)
        except PageNotAnInteger:
            geciList = paginator.page(1)
        except EmptyPage:
            geciList = paginator.page(paginator.num_pages)
        print(geciList)
        result['geciList'] = list(geciList)
        return JsonResponse(result,safe=False)
    else:
        print(request)

def logindo(request):
    if request.method == "POST":
        result = {}
        if not any(request.POST.get("user")) or (not any(request.POST.get("password"))):
            result["loginflag"] = "2"
            return JsonResponse(result, safe=False)
        ret2 = models.test.objects.filter(username= request.POST.get("user")).values()
        passworddict = ret2[0]
        if passworddict['password'] == request.POST.get("password"):
            result["loginflag"] = "1"
            return JsonResponse(result, safe=False)
        else:
            result["loginflag"] = "2"
            return JsonResponse(result, safe=False)
    else:
        print(request)

def registerdo(request):
    if request.method == "POST":
        test = models.test()
        result = {}
        #print(any(request.POST.get("username")))
        if not any(request.POST.get("username")) or (not any(request.POST.get("password")))\
                or (not any(request.POST.get("email"))) or (not any(request.POST.get("radio"))):
            result["registerflag"] = "2"
            result["registermsg"] = "segments are not allowed null"
            return JsonResponse(result, safe=False)
        ret = models.test.objects.filter(Q(username=request.POST.get("username"))|
                                         Q(email=request.POST.get("email"))).values()
        print(any(ret))
        if any(ret):
            result["registerflag"] = "2"
            result["registermsg"] = "username or email Repeated"
            return JsonResponse(result, safe=False)
        test.email = request.POST.get("email")
        test.lrrq = datetime.now()
        test.password = request.POST.get("password")
        test.username = request.POST.get("username")
        test.sex = request.POST.get("radio")
        try:
            registerflag = test.save()
        except Exception as e:
            result["registerflag"] = "2"
            return JsonResponse(result, safe=False)
            raise e
        if registerflag is None:
            result["registerflag"] = "1"
        return JsonResponse( result, safe=False)
    else:
        print(request)

def test_delete(request):
    if request.method == "POST":
        test = models.test.objects.filter(id = '2')
        for i  in test:
            i.delete()
        return HttpResponse("111")
    else:
        print(request)


def test_update(request):
    if request.method == "POST":
        test = models.test.objects.filter(id = "1")
        for i in test:
            i.username = request.POST.get("username")
            i.save()
        return HttpResponse("2222")
    else:
        print(request)