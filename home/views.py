from django.shortcuts import render
from .models import CarsModel
from rest_framework.response import Response
from .sirelizers import CarsSerializers
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet


class CarsView(APIView):
    def post(self, request):
        data = request.data
        serializer = CarsSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "DONE!"})
        else:
            return Response(serializer.errors)
