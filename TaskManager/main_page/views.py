from django.shortcuts import render
from django.http import HttpResponse


def tasks(request):
    return render(request, 'main_page/tests.html')
