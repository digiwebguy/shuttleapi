from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShuttleStation
from .serializers import ShuttleStationSerializer
from .serializers import ShuttleStationAlertsSerializer


class ShuttleStationsList(APIView):

    def get(self, request):
        shuttleStations = ShuttleStation.objects.all()
        serializer = ShuttleStationSerializer(shuttleStations, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class PendingAlertsInShuttleStationsList(APIView):
    def get(self, request):
        shuttleStations = ShuttleStation.objects.all()
        # shuttleStations = ShuttleStation.objects.exclude(direction_options.option__exact="Towards Commercial")
        serializer = ShuttleStationAlertsSerializer(shuttleStations, many=True)
        return Response(serializer.data)

    def post(self):
        pass
