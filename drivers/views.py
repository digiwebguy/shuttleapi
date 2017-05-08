from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Driver
from .serializers import DriversSerializer

class DriversList(APIView):

    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriversSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self):
        pass
