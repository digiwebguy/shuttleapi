from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
# from .models import Timestamp
# from .serializers import TimestampSerializer
from django.utils import timezone
from django.http import HttpResponse


# timestamp/
class TimestampList(APIView):

    def get(self, request):
        cur_datetime = str(timezone.now())
        cur_datetime1 = cur_datetime[2:19]
        cur_datetime2 = cur_datetime[-6:-3]
        cur_datetime = cur_datetime1 + cur_datetime2
        cur_datetime = cur_datetime.replace('-', '/')
        cur_datetime = cur_datetime.replace(' ', ',')
        return HttpResponse(cur_datetime)

    def post(self, request):
        cur_datetime = str(timezone.now())
        cur_datetime1 = cur_datetime[2:19]
        cur_datetime2 = cur_datetime[-6:-3]
        cur_datetime = cur_datetime1 + cur_datetime2
        cur_datetime = cur_datetime.replace('-', '/')
        cur_datetime = cur_datetime.replace(' ', ',')
        return HttpResponse(cur_datetime)