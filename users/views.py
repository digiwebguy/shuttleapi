from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


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


# https://test-korba-api.herokuapp.com
class PayForTrips(APIView):
    def post(self, request):
        print(request.data)
        # card_number = request.data['card_number']

        # try:
        #     user = User.objects.get(index_number=card_number)
        # except User.DoesNotExist:
        #     return Response('User Doesnt exist',status=status.HTTP_404_NOT_FOUND)
        #
        # print(user)
        # user.amount -=1
        # user.save()
        for index_number in request.data:
            print(index_number + "; ")
            user = User.objects.get(index_number=index_number)
            print(user)
            print("old user amount" + str(user.amount))
            user.amount -= 1
            print("new user amount" + str(user.amount))
            user.save()
        serializer = UserSerializer(user)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)
