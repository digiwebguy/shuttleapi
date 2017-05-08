from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AlertStatus
from .serializers import AlertStatusSerializer

class ShuttleStationsList(APIView):

    def get(self, request):
        alertStatuses = AlertStatus.objects.all()
        serializer = AlertStatusSerializer(alertStatuses, many=True)
        return Response(serializer.data)

    def post(self):
        pass
