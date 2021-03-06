'''
Use django shell to run the script:
exec(open('./populate_database_utils/populate_database.py').read())

'''
import csv
from world_development_indicators_backend.models import WorldDevelopmentIndicators
from io import StringIO
import re

def create_wdi_database(row):
    WorldDevelopmentIndicators.objects.create(
                    country_name=row[0],
                    country_code=row[1],
                    indicator_name=row[2],
                    indicator_code=row[3],
                    y_1960=row[4],
                    y_1961=row[5],
                    y_1962=row[6],
                    y_1963=row[7],
                    y_1964=row[8],
                    y_1965=row[9],
                    y_1966=row[10],
                    y_1967=row[11],
                    y_1968=row[12],
                    y_1969=row[13],
                    y_1970=row[14],
                    y_1971=row[15],
                    y_1972=row[16],
                    y_1973=row[17],
                    y_1974=row[18],
                    y_1975=row[19],
                    y_1976=row[20],
                    y_1977=row[21],
                    y_1978=row[22],
                    y_1979=row[23],
                    y_1980=row[24],
                    y_1981=row[25],
                    y_1982=row[26],
                    y_1983=row[27],
                    y_1984=row[28],
                    y_1985=row[29],
                    y_1986=row[30],
                    y_1987=row[31],
                    y_1988=row[32],
                    y_1989=row[33],
                    y_1990=row[34],
                    y_1991=row[35],
                    y_1992=row[36],
                    y_1993=row[37],
                    y_1994=row[38],
                    y_1995=row[39],
                    y_1996=row[40],
                    y_1997=row[41],
                    y_1998=row[42],
                    y_1999=row[43],
                    y_2000=row[44],
                    y_2001=row[45],
                    y_2002=row[46],
                    y_2003=row[47],
                    y_2004=row[48],
                    y_2005=row[49],
                    y_2006=row[50],
                    y_2007=row[51],
                    y_2008=row[52],
                    y_2009=row[53],
                    y_2010=row[54],
                    y_2011=row[55],
                    y_2012=row[56],
                    y_2013=row[57],
                    y_2014=row[58],
                    y_2015=row[59],
                    y_2016=row[60],
                    y_2017=row[61],
                    y_2018=row[62],
                    y_2019=row[63],
                    # y_2020=row[64],
                )

CSV_PATH_POPULATION = 'populate_database_utils/population.csv'
CSV_PATH_GDP = 'populate_database_utils/gdp.csv'
CSV_PATH_CARBON = 'populate_database_utils/carbon.csv'
CSV_PATH_LE_MALE ='populate_database_utils/life_expectancy_male.csv'
CSV_PATH_HIGH_TECH = 'populate_database_utils/high_tech.csv'
CSV_PATH_PATENT_NONR = 'populate_database_utils/patent_nonres.csv'
CSV_PATH_PATENT_RES = 'populate_database_utils/patent_res.csv'

country_list = ['CHN', 'IND', 'MEX', 'NGA', 'USA']

csv.register_dialect('MyDialect', skipinitialspace=False, delimiter=',', quotechar='"', lineterminator='\r\n')

# For total population
with open(CSV_PATH_POPULATION, 'r', encoding='UTF-8') as csvfile:
    data = csv.reader(csvfile, dialect='MyDialect')
    for row in data:
        if row[1] in country_list:
            create_wdi_database(row)

# For GDP
with open(CSV_PATH_GDP, 'r', encoding='UTF-8') as csvfile:
    data = csv.reader(csvfile, dialect='MyDialect')
    for row in data:
        if row[1] in country_list:
            create_wdi_database(row)

# For CO2 emission
with open(CSV_PATH_CARBON, 'r', encoding='UTF-8') as csvfile:
    data = csv.reader(csvfile, dialect='MyDialect')
    for row in data:
        if row[1] in country_list:
            create_wdi_database(row)

# Life expectancy of male
with open(CSV_PATH_LE_MALE, 'r', encoding='UTF-8') as csvfile:
    data = csv.reader(csvfile, dialect='MyDialect')
    for row in data:
        if row[1] in country_list:
            create_wdi_database(row)

# High technology exports
with open(CSV_PATH_HIGH_TECH, 'r', encoding='UTF-8') as csvfile:
    data = csv.reader(csvfile, dialect='MyDialect')
    for row in data:
        if row[1] in country_list:
           create_wdi_database(row)

# For Patent application non-residents
with open(CSV_PATH_PATENT_NONR, 'r', encoding='UTF-8') as csvfile:
    data = csv.reader(csvfile, dialect='MyDialect')
    for row in data:
        if row[1] in country_list:
            create_wdi_database(row)

# For Patent application residents
with open(CSV_PATH_PATENT_RES, 'r', encoding='UTF-8') as csvfile:
    data = csv.reader(csvfile, dialect='MyDialect')
    for row in data:
        if row[1] in country_list:
            create_wdi_database(row)

# WorldDevelopmentIndicators.objects.all().delete()