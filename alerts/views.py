from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alert
from .serializers import AlertSerializer
from datetime import datetime
from alert_statuses.models import AlertStatus
from drivers.models import Driver

class AlertsList(APIView):

    def get(self, request):
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PendingAlertsList(APIView):

    def get(self, request):
        alerts = Alert.objects.filter(status_id=2)
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)



class AcceptAlerts(APIView):

    def post(self, request):
        print(request.data)

        alert_ids = request.data['alert_ids']
        driver_id = request.data['driver_id']
        driver = Driver.objects.get(id=driver_id)
        print(alert_ids)
        alert_status = AlertStatus.objects.get(id=2)
        print("alert_status")
        print(alert_status)

        for alert_id in alert_ids:
            alert = Alert.objects.get(id=alert_id)
            print("old alert")
            print(alert)
            alert.status_id = alert_status
            alert.driver_accepted_id = driver
            alert.accepted_time = datetime.now()
            print("new alert")
            print(alert)
            alert.save()

        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = "alerts accepted successfully"
        return Response(request.data, status=status.HTTP_200_OK)
