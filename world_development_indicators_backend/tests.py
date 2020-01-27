from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import WorldDevelopmentIndicators
from .serializers import WdiSerializer

# Create your tests here.

# class BaseViewTest(APITestCase):
#     client = APIClient()

#     @staticmethod
#     def create_song(title="", artist=""):
#         if title != "" and artist != "":
#             Songs.objects.create(title=title, artist=artist)
    
#     def setUp(self):
#         self.create_song("like glue", "sean paul")
#         self.create_song("like glue", "sean paul")
#         self.create_song("like glue", "sean paul")
#         self.create_song("like glue", "sean paul")


class GetAllSongsTest():

    def test_get_all_data(self):
        '''
        This test ensures that all data added exist when we make a GET request to the /display_data endpoint
        '''

        # The API endpoint
        response = self.client.get(
            reverse("wdi-all", kwargs={"version": "v1"})
        )
        # Fetch data from db
        expected = WorldDevelopmentIndicators.objects.all()
        serialized = WdiSerializer(expected, mana=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
