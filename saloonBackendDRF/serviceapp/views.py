from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from serviceapp.serializers import SeviceSerializer
from serviceapp.models import Service

#get method
class serapi(APIView): 
   def get(self,request,format=None): 
        es=Service.objects.all()
        eserialize=SeviceSerializer(es,many=True)

        return Response({'msg':'Welcome to Luxe Beaute ','service':eserialize.data}) 
