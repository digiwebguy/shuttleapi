from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Topup
from .serializers import TopupsSerializer
from vouchers.models import Voucher
from users.models import User
from topups.serializers import TopupsSerializer



class TopupsList(APIView):
    def get(self, request):
        topups = Topup.objects.all()
        serializer = TopupsSerializer(topups, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data['voucher_code'])
        voucher_code = request.data['voucher_code']
        user_id = request.data['user_id']

        try:
            voucher = Voucher.objects.get(voucher_code=voucher_code, is_active=1)
        except Voucher.DoesNotExist:
            response_data = {}
            response_data['error'] = "Error"
            response_data['message'] = "Incorrect Voucher Entered"
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        print(voucher.amount)
        amount_purchased = voucher.amount

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            response_data = {}
            response_data['error'] = "Error"
            response_data['message'] = "User doesn't exist in database"
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        user.amount +=amount_purchased
        user.save()

        voucher.is_active = 0
        voucher.save()

        topup_data = {}
        topup_data['user_id'] = user_id
        topup_data['amount'] = amount_purchased
        topup_data['payment_type'] = "VCH"
        topup_data['voucher_id'] = voucher.id

        topup_serializer = TopupsSerializer(data=topup_data)
        if topup_serializer.is_valid():
            topup_serializer.save()
            return Response(topup_serializer.data, status=status.HTTP_201_CREATED)
        return Response(topup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        print(topup_data)


        response_data = {}
        response_data['success'] = "Success"
        response_data['message'] = "Topup Successful"
        return Response(response_data, status=status.HTTP_200_OK)
