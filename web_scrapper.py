from typing import Tuple
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import statistics
# from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

URL = "https://www.worldometers.info/world-population/population-by-country/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("tbody")

row = results.find_all("tr")

insert_arr = []

def db():
    return mysql.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWD,
                         db=DB_NAME)

def scape(row):
    for element in row:
        row_list = []
        country = element.find("a")
        country = country.text
        pop = element.find_all("td")[2]
        pop = pop.text
        pop = pop.replace(",","")
        # print(country.strip())
        # print(pop.strip())
        # print()
        row_list.insert(0, country)
        row_list.insert(1, int(pop))
        row_list.insert(2, 2020)
        insert_arr.append(tuple(row_list))

scape(row)
# # print(tuple(rowlist))

sql_q = """insert into population (country, population, year)
             values(%s, %s, %s)"""
connect = db()
cursor = connect.cursor()

cursor.execute("DELETE FROM population")

cursor.executemany(sql_q, insert_arr)
connect.commit()


    