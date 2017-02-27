from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Topup
from .serializers import TopupsSerializer
# trips/
class TopupsList(APIView):

    def get(self, request):
        topups = Topup.objects.all()
        serializer = TopupsSerializer(topups, many=True)
        return Response(serializer.data)

    def post(self):
        pass
