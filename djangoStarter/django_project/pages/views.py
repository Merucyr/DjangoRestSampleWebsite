from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import *

@api_view(['POST'])
def CreatePerson(request):
    if request.method == 'POST':
        newPerson = NewAPIPersonSerializer(data=request.data) 
        if newPerson.is_valid():
            newPerson.save()
            return Response(newPerson.data)
        return Response(newPerson.errors)

@api_view(['GET'])
def PersonList(request):
    people = NewAPIPerson.objects.all()
    serializer = NewAPIPersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PersonDetail(request,personid):
    person = NewAPIPerson.objects.get(id=personid)
    serializer = NewAPIPersonSerializer(person, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getRoutes(request):
 routes = [  
  {  
   'Endpoint': '/people/',  
   'method': 'GET',  
   'body': None,  
   'description': 'Returns the list (array) of all people'  
  },  
  {  
   'Endpoint': '/create/',  
   'method': 'POST',  
   'body': {'body': ""},  
   'description': 'Creates a new person object'  
  },  
  {  
   'Endpoint': '/people/id/',  
   'method': 'GET',  
   'body': None,  
   'description': 'Returns a single person object'  
  }
 ]
 return Response(routes)