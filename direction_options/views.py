from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DirectionOption
from .serializers import DirectionOptionSerializer


class DirectionOptionsList(APIView):

    def get(self, request):
        directionOptions = DirectionOption.objects.all()
        serializer = DirectionOptionSerializer(directionOptions, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class DirectionOptionsByShuttleStationId(APIView):

    def get(self, request, pk):
        directionOptions = DirectionOption.objects.filter(shuttle_station_id=pk)
        serializer = DirectionOptionSerializer(directionOptions, many=True)
        return Response(serializer.data)

    def post(self):
        pass
