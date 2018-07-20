from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. Ann rocks.")

def sms(request):
    twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')

