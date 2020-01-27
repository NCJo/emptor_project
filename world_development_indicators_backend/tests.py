from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import WorldDevelopmentIndicators
from .serializers import WdiSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_data(country_name="", country_code="", indicator_name="",
                    data_type="", indicator_code="",
                    y_1960="", y_1961="", y_1962="", y_1963="", y_1964="", y_1965="",
                    y_1966="", y_1967="", y_1968="", y_1969="", y_1970="", y_1971="",
                    y_1972="", y_1973="", y_1974="", y_1975="", y_1976="", y_1977="",
                    y_1978="", y_1979="", y_1980="", y_1981="", y_1982="", y_1983="",
                    y_1984="", y_1985="", y_1986="", y_1987="", y_1988="", y_1989="",
                    y_1990="", y_1991="", y_1992="", y_1993="", y_1994="", y_1995="",
                    y_1996="", y_1997="", y_1998="", y_1999="", y_2000="", y_2001="",
                    y_2002="", y_2003="", y_2004="", y_2005="", y_2006="", y_2007="",
                    y_2008="", y_2009="", y_2010="", y_2011="", y_2012="", y_2013="",
                    y_2014="", y_2015="", y_2016="", y_2017="", y_2018="", y_2019="",
                    y_2020=""):
        if country_name != "" and country_code != "":
            WorldDevelopmentIndicators.objects.create(
                country_name=country_name,
                country_code=country_code,
                indicator_name=indicator_name,
                data_type=data_type,
                indicator_code=indicator_code,
                y_1960=y_1960
            )
    
    def setUp(self):
        self.create_data("Test Country", "TC", "Testing", "Type if data", "TEST.CODE", "788778.8989")


class GetAllDataTest(BaseViewTest):

    def test_get_all_data(self):
        '''
        This test ensures that all data added exist when we make a GET request to the /display_data endpoint
        '''

        # The API endpoint
        response = self.client.get(
            reverse("wdi-all")
        )
        # Fetch data from db
        expected = WorldDevelopmentIndicators.objects.all()
        serialized = WdiSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
