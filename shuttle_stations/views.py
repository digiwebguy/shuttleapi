from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShuttleStation
from .serializers import ShuttleStationSerializer

class ShuttleStationsList(APIView):

    def get(self, request):
        shuttleStations = ShuttleStation.objects.all()
        serializer = ShuttleStationSerializer(shuttleStations, many=True)
        return Response(serializer.data)

    def post(self):
        pass
