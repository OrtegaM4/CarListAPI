from django.contrib.auth.models import User
from rest_framework import generics
from .models import Cars
from .serializers import CarSerializer #UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class CarsList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    List all cars, or create a new cars.
    """
    def get(self, request, format=None):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    Provides a get method handler.
    """
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class CarsDetail(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    """
    Retrieve, update or delete a cars instance.
    """
    def get_object(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cars = self.get_object(pk)
        serializer = CarSerializer(cars)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cars = self.get_object(pk)
        serializer = CarSerializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cars = self.get_object(pk)
        Cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
