from rest_framework.serializers import ModelSerializer

from .models import WorldDevelopmentIndicators

class WdiSerializer(ModelSerializer):
    class Meta:
        model = WorldDevelopmentIndicators
        fields = (
            'country_name', 'country_code', 'indicator_name', 'data_type', 'indicator_code', 'y_1960', 'y_1961', 'y_1962', 'y_1963', 'y_1964', 'y_1965', 'y_1966', 'y_1967', 'y_1968', 'y_1969', 'y_1970', 'y_1971', 'y_1972', 'y_1973', 'y_1974', 'y_1975', 'y_1976', 'y_1977', 'y_1978', 'y_1979', 'y_1980', 'y_1981', 'y_1982', 'y_1983', 'y_1984', 'y_1985', 'y_1986', 'y_1987', 'y_1988', 'y_1989', 'y_1990', 'y_1991', 'y_1992', 'y_1993', 'y_1994', 'y_1995', 'y_1996', 'y_1997', 'y_1998', 'y_1999', 'y_2000', 'y_2001', 'y_2002', 'y_2003', 'y_2004', 'y_2005', 'y_2006', 'y_2007', 'y_2008', 'y_2009', 'y_2010', 'y_2011', 'y_2012', 'y_2013', 'y_2014', 'y_2015', 'y_2016', 'y_2017', 'y_2018', 'y_2019',     
        )