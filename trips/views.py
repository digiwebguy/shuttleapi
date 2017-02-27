from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from .serializers import TripsSerializer
# trips/
class TripsList(APIView):

    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripsSerializer(trips, many=True)
        return Response(serializer.data)

    def post(self):
        pass
