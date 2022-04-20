from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from environment.models import Environment
from environment.serializer import enironmentSerializer

from django.core.files.storage import default_storage

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view





@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
  if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = enironmentSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):

    if request.method == 'GET':
        tutorial = Environment.objects.get(pk=pk)

        tutorial_serializer = enironmentSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)
"""
@csrf_exempt
def environmentApi(request,id=1):
    if request.method=='GET':
        departments = Environment.objects.all()
        departments_serializer=enironmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=enironmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Environment.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=enironmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Environment.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)"""