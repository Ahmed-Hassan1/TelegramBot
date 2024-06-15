from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import urllib.parse
import json
# Create your views here.

@csrf_exempt
def botRecieve(request):
    print(type(request.body))
    stri=request.body.decode("utf-8")
    #print(type(stri))
    encoded=urllib.parse.quote(stri)
    requests.get('https://api.telegram.org/bot6608065982:AAFn1YaJ0iuBHGhIokuvBOhwo5ILVwnADWY/sendMessage?chat_id=-1002010779106&text='+encoded)
    return HttpResponse("Hello")