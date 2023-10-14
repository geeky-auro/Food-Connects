from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("The Food We Serve is the Love we feed!")