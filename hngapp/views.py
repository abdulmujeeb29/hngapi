from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework import status 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
# Create your views here.

#endpoint to create a user 
@api_view(['POST'])
def create_person(request):
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#endpoint to get all users 
@api_view(['GET'])
def get_person(request):
    person = Person.objects.all()
    serializer =PersonSerializer(person,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)




#endpoint to get,update and delete using name as the dynmic parameter 
@api_view(['GET', 'DELETE', 'PUT'])
def get_person_by_name(request,person_name):
    try:
        person = Person.objects.get(name=person_name)

    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=404)
    
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data,status=200)
    
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        person.delete()
        return Response({"message": "Person deleted"}, status=204)



#using id as dynamic parameter 
@api_view(['GET', 'PUT', 'DELETE'])
def get_person_by_id(request, person_id):
    try:
        person = get_object_or_404(Person, id=person_id)
    except Person.DoesNotExist:
        return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        person.delete()
        return Response({"message": "Person deleted"}, status=status.HTTP_204_NO_CONTENT)