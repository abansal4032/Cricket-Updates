from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def commentary(request):
    url = "http://push.cricbuzz.com/match-api/16870/commentary.json"
    response = requests.get(url)
    return HttpResponse(response.text)