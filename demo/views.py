from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Demo
from .serializers import DemoSerializer
# trips/
class DemoList(APIView):

    def get(self, request):
        demos = Demo.objects.all()
        serializer = DemoSerializer(demos, many=True)
        return Response(serializer.data)

    def post(self):
        pass

    def put(self, request,pk=None):
        try:
            demos = Demo.objects.get(id=pk)
        except Demo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DemoSerializer(demos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TurnOnLights(APIView):

#     def get(self, request):
#         try:
#             demos = Demo.objects.filter(pk=1)
#         except Demo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         print(demos)
#         serializer = DemoSerializer(demos, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass