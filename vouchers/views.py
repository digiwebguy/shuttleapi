from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Voucher
from .serializers import VoucherSerializer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
import json


class VoucherList(APIView):

    def get(self, request):
        vouchers = Voucher.objects.all()
        serializer = VoucherSerializer(vouchers, many=True)
        return Response(serializer.data)


class TopUpWithVoucher (APIView):
    def post(self, request):
        return Response(request.data, status=status.HTTP_200_OK)