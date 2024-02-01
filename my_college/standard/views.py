from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from standard.models import Section,Student
from standard.serializers import SectionSerializer,StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class SectionViewSet(viewsets.ModelViewSet):
    queryset=Section.objects.all()
    serializer_class=SectionSerializer
    @action(detail=True,methods=['get'])
    def students(self,request,pk=None):
        #getting students in the particular section
        try:
            section=Section.objects.get(pk=pk)
            studs=Student.objects.filter(section=section)
            studs_serializer=StudentSerializer(studs,many=True,context={'request':request})
            return Response(studs_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':"section doesnot exists"
            })


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer