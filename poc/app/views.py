import os
import subprocess
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.exceptions import NotFound
from .models import Poc
from .serializers import PocSerializer

class PocApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        pocs = Poc.objects.all()
        serializer = PocSerializer(pocs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        #time = datetime.datetime.fromtimestamp(os.system('date +%s')) # +"%FT%T"'))
        #getTime = subprocess.check_output('date +"%FT%T%z-0300"', shell=True)
        #getTime.strftime('%Y-%m-%dThh:mm')
        data = request.data #{"currentTime" : getTime} # request.data
        serializer = PocSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PocDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Poc.objects.get(pk=pk)
        except Poc.DoesNotExist:
            raise NotFound()
        
    def get(self, request, pk):
        poc = self.get_object(pk)
        serializer = PocSerializer(poc)
        return Response(serializer.data)
        
    def put(self, request, pk):
        poc = self.get_object(pk)
        serializer = PocSerializer(poc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poc = self.get_object(pk)
        poc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
            