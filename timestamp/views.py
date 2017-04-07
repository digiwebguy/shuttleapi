from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
# from .models import Timestamp
# from .serializers import TimestampSerializer
import datetime


# timestamp/
class TimestampList(APIView):

    def get(self, request):
        return Response(datetime.datetime.now())

    def post(self, request):
        pass