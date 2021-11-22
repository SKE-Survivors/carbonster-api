import sys
from flask import abort
import pymysql as mysql
from datetime import datetime
import statistics
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

def db_cursor():
    return mysql.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWD,
                         db=DB_NAME).cursor()

def find_min(arr):
    min = arr[0]
    for i in range(0, len(arr)):       
        if(arr[i] < min):    
            min = arr[i];   
    return min 
    
def find_max(arr):
    max = arr[0]
    for i in range(0, len(arr)):       
        if(arr[i] > max):    
            max = arr[i];   
    return max 

def find_stat(arr):
    min = find_min(arr)
    max = find_max(arr)
    avg = sum(arr)/len(arr)
    range = max - min
    var = statistics.pvariance(arr)
    sd = statistics.pstdev(arr)
    return min, max, avg, range, var, sd

def get_air(country):
    with db_cursor() as cs:
        cs.execute("""
            SELECT c.country, c.carbon_avg, o.ozone_avg, m.methane_avg
            FROM carbontest AS c
            INNER JOIN ozonetest AS o 
            ON c.start >= o.start and c.start <= o.end
            INNER JOIN mettest AS m
            ON o.start >= m.start and o.start <= m.end
            WHERE c.country = %s       
            """, [country])
        result = cs.fetchone()
    if result:
        country, co, me, oz = result
        return models.Quality(*result)
    else:
        abort(404)
        
def get_air_statistic_carbon(country):
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    with db_cursor as cs:
        cs.execute("""
            SELECT *
            FROM carbontest c 
            WHERE MONTH(c.end) = %s 
            AND YEAR(c.end) = %s 
            AND c.country = %s
            """, [curr_month, curr_year, country])
        result = cs.fetchall()
        daily = []
        for element in result:
            daily.append(element[2])
                    
        result = [models.Statistic(country, find_stat(daily))]
        return result
    
def get_air_statistic_methane(country):
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    with db_cursor as cs:
        cs.execute("""
            SELECT *
            FROM mettest c 
            WHERE MONTH(c.end) = %s 
            AND YEAR(c.end) = %s 
            AND c.country = %s
            """, [curr_month, curr_year, country])
        result = cs.fetchall()
        daily = []
        for element in result:
            daily.append(element[2])
                    
        result = [models.Statistic(country, find_stat(daily))]
        return result
    
def get_air_statistic_ozone(country):
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    with db_cursor as cs:
        cs.execute("""
            SELECT *
            FROM ozonetest c 
            WHERE MONTH(c.end) = %s 
            AND YEAR(c.end) = %s 
            AND c.country = %s
            """, [curr_month, curr_year, country])
        result = cs.fetchall()
        daily = []
        for element in result:
            daily.append(element[2])
            
        result = [models.Statistic(country, find_stat(daily))]
        return result

def get_emission(country):
    with db_cursor as cs:
        cs.execute("""
            SELECT c.country, c.carbonIntensity
            FROM carbonIntensitytest c
            WHERE c.country = %s       
            """, [country])
        result = cs.fetchone()
    if result:
        country, inten = result
        return models.Emission(*result)
    else:
        abort(404)

def get_emission_per_person(country):
    with db_cursor as cs:
        cs.execute("""
            SELECT c.code, p.population, ci.carbonIntensity
            FROM code c
            INNER JOIN population p
            ON c.country = p.country
            INNER JOIN carbonIntensitytest ci
            ON ci.country = c.code
            WHERE c.code = %s     
            """, [country])
        result = cs.fetchone()
    if result:
        code, pop, carin = result
        per = carin/pop
        return models.Emission(code, per)
    else:
        abort(404)
    
def get_correlation_carbon(country):
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    with db_cursor as cs:
        cs.execute("""
            SELECT c.code, p.population, ct.carbon_avg
            FROM code c
            INNER JOIN population p
            ON c.country = p.country
            INNER JOIN carbontest ct
            ON ct.country = c.code
            WHERE MONTH(ct.end) = %s 
            AND YEAR(ct.end) = %s 
            WHERE c.code = %s
            """, [curr_month, curr_year, country])
        result = cs.fetchall()
        pop = result[-1][1]
        daily = []
        for element in result:
            daily.append(element[2])
        car = sum(daily)
        corr = statistics.correlation(pop, car)    
        result = [models.Correlation(country, corr)]
        return result