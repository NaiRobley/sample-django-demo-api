from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer
import json


# Create your views here.

def home(request):
    return HttpResponse('Welcome to the Students API')


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all students
    """
    if request.method == "GET":
        studs = Student.objects.all()
        serializer = StudentSerializer(studs, many=True)
        return Response(serializer.data)


    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        dta = data["id"]
        try:
            std = Student.objects.get(id=dta)
            names = "First Name: "+std.first_name + ". Last Name: " + std.last_name

            return Response(names, status=status.HTTP_200_OK)

        except:
            return Response("Student with the id has not been found", status=status.HTTP_404_NOT_FOUND)

        # serializer = StudentSerializer(data=request.DATA)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])


def student(request, id):
    obj = Student.objects.get(id=id)
    firstName = obj.first_name
    lastName = obj.last_name
    uni = str(obj.university)
    details = "Names: " + firstName + " " + lastName + "<br>University: " + uni
    parsedData = json.dumps({"Names":(firstName+ " "+lastName), "Univeristy":uni}, sort_keys=True, indent=4)

    return HttpResponse(parsedData)


def university(request, id):
    unii = University.objects.get(id=id)
    uniName = unii.name
    uniID = unii.id
    parsedData = json.dumps({"Names":uniName, "ID":uniID}, sort_keys=True, indent=4)
    return HttpResponse(parsedData)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer