from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
import json


# users/
class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PayForTrips(APIView):
    def post(self, request):
        print(request.data)
        card_number = request.data['card_number']

        try:
            user = User.objects.get(index_number=card_number)
        except User.DoesNotExist:
            response_data = {}
            response_data['result'] = 'error'
            response_data['message'] = 'User Does Not Exist'
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)

        print(user)
        if user.amount < 1:
            response_data = {}
            response_data['result'] = 'failure'
            response_data['message'] = 'Insufficient Funds'
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            user.amount -=1
            user.save()
            response_data = {}
            response_data['result'] = 'success'
            response_data['message'] = 'Payment Successful'
            return Response(response_data, status=status.HTTP_200_OK)






            # for index_number in request.data:
            #     print(index_number + "; ")
            #     user = User.objects.get(index_number=index_number)
            #     print(user)
            #     print("old user amount" + str(user.amount))
            #     user.amount -= 1
            #     print("new user amount" + str(user.amount))
            #     user.save()
            # serializer = UserSerializer(user)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)