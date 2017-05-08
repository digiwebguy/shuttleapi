from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alert
from .serializers import AlertSerializer

class AlertsList(APIView):

    def get(self, request):
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)

    def post(self):
        pass
