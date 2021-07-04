from django.shortcuts import render
from django.http import HttpResponse


def tasks(request):
    return HttpResponse("<h4>Hello, World!</h4>")
