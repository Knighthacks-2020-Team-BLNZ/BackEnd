from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def account(request):
  return JsonResponse(
      {
        "name": "testuser",
        "type": "student"
        }
  )

def helloworld(request):
    return HttpResponse("Hello, world. This is a test view - Basic http response.")