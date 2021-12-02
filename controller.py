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
        if (arr[i] < min):
            min = arr[i]
    return min


def find_max(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        if (arr[i] > max):
            max = arr[i]
    return max


def find_stat(arr):
    min = find_min(arr)
    max = find_max(arr)
    avg = sum(arr) / len(arr)
    range = max - min
    var = statistics.pvariance(arr)
    sd = statistics.pstdev(arr)
    return min, max, avg, range, var, sd


def get_air(country):
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT DISTINCT c.country, c.carbon_avg, m.methane_avg, o.ozone_avg, c.start
            FROM carbontest AS c
            INNER JOIN ozonetest AS o
            ON c.start = o.start and o.country = c.country
            INNER JOIN mettest AS m
            ON o.start = m.start and o.country = m.country
            WHERE c.country = %s
            """, [country])
        result = cs.fetchall()
    if result:
        return [
            models.Quality(row[0], row[1], row[2], row[3], row[4].date())
            for row in result
        ]
    else:
        abort(404)


def get_th_air(province):
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT DISTINCT c.district, AVG(c.carbon), AVG(o.ozone), AVG(m.methane), DATE(c.ts)
            FROM carbonTHapi AS c
            INNER JOIN ozoneTHapi AS o
            ON DATE(c.ts) = DATE(o.ts) and o.district = c.district
            INNER JOIN methaneTHapi AS m
            ON DATE(o.ts) = DATE(m.ts) and o.district = m.district
            WHERE c.district = %s
            GROUP BY DATE(c.ts)
            """, [province])
        result = cs.fetchall()
    if result:
        return [
            models.Quality(row[0], row[1], row[2], row[3], row[4])
            for row in result
        ]
    else:
        abort(404)


def get_air_statistic_carbon(country):
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT c.carbon_avg
            FROM carbontest c
            WHERE MONTH(c.end) = 11
            AND YEAR(c.end) = 2021
            AND c.country = %s
            """, [country])
        result = cs.fetchall()
        daily = []
        for element in result:
            daily.append(element[0])

        c_min, c_max, avg, c_range, var, sd = find_stat(daily)
        # c_min, c_max, avg, c_range, var, sd = 1,2,3,4,5,6
        result = [
            models.Statistic(country, c_min, c_max, avg, c_range, var, sd)
        ]
        return result


def get_air_statistic_methane(country):
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT *
            FROM mettest c
            WHERE MONTH(c.end) = 11
            AND YEAR(c.end) = 2021
            AND c.country = %s
            """, [country])
        result = cs.fetchall()
        daily = []
        for element in result:
            daily.append(element[2])

        c_min, c_max, avg, c_range, var, sd = find_stat(daily)
        result = [
            models.Statistic(country, c_min, c_max, avg, c_range, var, sd)
        ]
        return result


def get_air_statistic_ozone(country):
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT *
            FROM ozonetest c
            WHERE MONTH(c.end) = 11
            AND YEAR(c.end) = 2021
            AND c.country = %s
            """, [country])
        result = cs.fetchall()
        daily = []
        for element in result:
            daily.append(element[2])

        c_min, c_max, avg, c_range, var, sd = find_stat(daily)
        result = [
            models.Statistic(country, c_min, c_max, avg, c_range, var, sd)
        ]
        return result


def get_emission(country):
    # exec(open("web_scrapper.py").read())
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT c.country, c.carbonIntensity
            FROM carbonIntensitytest c
            WHERE c.country = %s
            """, [country])
        result = cs.fetchone()
    if result:
        return [models.Emission(*result)]
    else:
        abort(404)


def get_emission_per_person(country):
    # exec(open("web_scrapper.py").read())
    with db_cursor() as cs:
        cs.execute(
            """
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
        per = carin / pop
        return [models.Emission(code, per)]
    else:
        abort(404)


def get_correlation_carbon():
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    # exec(open("web_scrapper.py").read())
    with db_cursor() as cs:
        cs.execute(
            """
            SELECT c.code, p.population, SUM(ct.carbon_avg)
            FROM code c
            INNER JOIN population p
            ON c.country = p.country
            INNER JOIN carbontest ct
            ON ct.country = c.code
            WHERE MONTH(ct.end) = 11 
            AND YEAR(ct.end) = 2021 
            GROUP BY c.code, p.population
            """)
        result = cs.fetchall()
        return [models.Correlation(row[0], row[1], row[2]) for row in result]
