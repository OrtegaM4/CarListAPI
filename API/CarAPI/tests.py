from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Cars
from .serializers import CarSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client= APIClient()
    @staticmethod

    def create_car(make='',name='',horsepower=''):
        if make != "" and name !="" and horsepower!="":
            Cars.objects.create(make=make, name=name,horsepower=horsepower)

    def setUp(self):
        #add test data
        self.create_car(make='toyota',name='FRS', horsepower='200')
        self.create_car(make='subbie',name='brz', horsepower='200')
        self.create_car(make='Honda',name='accord', horsepower='220')
        self.create_car(make='Nissan',name='altima', horsepower='230')

class GetAllCarsTest(BaseViewTest):

    def test_get_all_cars(self):
        """
        This function ensures that all cars added in the setup method
        exist when we make a get request to the cars/endpoint
        """
        # #Hit the API endpoint
        # #response = self.client.get(
        #     #reverse("cars-all",kwargs={"version":"v1"})
        # )

        #Fetch the data from data base

        expected= Cars.objects.all()
        serialized= CarSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
