from django.shortcuts import render
from django.http import HttpResponse


def student():
    return HttpResponse("Student list")
