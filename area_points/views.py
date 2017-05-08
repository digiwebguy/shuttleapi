from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AreaPoint
from .serializers import AreaPointSerializer

class AreaPointsList(APIView):

    def get(self, request):
        areaPoints = AreaPoint.objects.all()
        serializer = AreaPointSerializer(areaPoints, many=True)
        return Response(serializer.data)

    def post(self):
        pass
