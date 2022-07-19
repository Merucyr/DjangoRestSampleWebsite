from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def hpResponse(request):
    return Response("This is the homepage! Check out some of the api calls by breaking the website or something")