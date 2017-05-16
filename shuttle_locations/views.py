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

    def put(self, request,pk=None):
        try:
            shuttleLocation = ShuttleLocation.objects.get(driver_id=pk)
        except ShuttleLocation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ShuttleLocationSerializer(shuttleLocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
