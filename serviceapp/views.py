from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

def index(request):
    return HttpResponse('ho')
