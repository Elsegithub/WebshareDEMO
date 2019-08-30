from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from myapp import models
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
        ret = models.textvue.objects.all().values()
        print(list(ret))
        result = {"geciList":list(ret)}
        return JsonResponse(result,safe=False)
    else:
        print(request)

def test_list(request):
    ret = models.test.objects.all().order_by("id").values()
    ret2 = models.test.objects.filter(id= '1').values()
    # for i in ret:
    #     print(i.username)
    #     print(i.password)
    #     print(i.lrrq)
    #     print(i.email)
    ret_list = list(ret)
    ret_list_id = list(ret2)
    print(ret2)
    print(ret_list_id)
    print(ret_list)
    result = {"ret_list": ret_list, "ret_list_id" : ret_list_id}
    return  JsonResponse(result, safe=False)

def test_insert(request):
    if request.method == "POST":
        test = models.test()
        test.email = "9999999"
        test.lrrq = datetime.now()
        test.password = "111111"
        test.username = "122222"
        test.sex = "女"
        test.save()
        return HttpResponse("12312")
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