from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShuttleLocation
from .serializers import ShuttleLocationSerializer

class ShuttleLocationsList(APIView):

    def get(self, request):
        shuttleLocations = ShuttleLocation.objects.all()
        serializer = ShuttleLocationSerializer(shuttleLocations, many=True)
        return Response(serializer.data)

    def post(self):
        pass
