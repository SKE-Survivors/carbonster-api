# Carbonster API

## Members

- 6210545475 Nutta Sittipongpanich
- 6210545505 Nanthakarn Limkool
- 6210545611 Sahadporn Charnlertlakha

SKE17 Kasetsart University

## Overview

[Presentation slide](https://drive.google.com/file/d/1TIyIySlGJfEID2mTeglj6w8EQ-9uLhL-/view?usp=sharing)

### Motivation

Air pollution has become a big issue all over the world and In class assignment about pm2.5 has become a motivation to research about carbon emission because it is a big factor of air quality measure too.

### Goal

To provide information about carbon emissions and gas in Thailand and global to determine air quality in different perspective than PM2.5.

### Feature

- Statistic of CO CH4 O3 in each country
- Air quailty
  - Average CO CH4 O3 volume of each country
  - Average CO CH4 O3 volume in Thailand provinces (Bangkok\*, Narathiwat, Khon Kaen, Rayong, Chiang Mai)
- Correlation between Carbon emissions and population of each country
- Carbon emission, CO, CH4, O3 of each country
- Carbon emission per person

Note: Bangkok\* is the data collected from KidBright

## Requirements

### Libraries

- OpenAPI-to-GraphQL
- PyMySQL

### Tools

- Python 3.6++
- HTML CSS Javascript
- Chart js
- Plotly
- Node-RED
- KidBright 32 V1.5i
- MQ-5 sensor
- ADS1115

## Installation

- Clone this github project/ download ZIP file

```bash
$ git clone https://github.com/SKE-survivors/carbonster-api.git
```

- Download `OpenAPI-to-GraphQL`

```bash
# [if not yet have it] install OpenAPI-to-GraphQL
$ npm install -g openapi-to-graphql-cli@2.5.0
```

- Download/add `openapi-generator-cli-4.3.1.jar` to the project and download required libraries

```bash
# generate,update /autogen
$ java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/carbonster-api.yaml -o autogen -g python-flask

$ cd autogen
$ pip install -r requirements.txt

# start sever
$ python -m openapi_server
# If above command didn't work use this instead
$ python app.py
```

Run [app.py](app.py)

Go to <http://localhost:8000/carbonster/v1/ui> to open Swagger

Then open another terminal

```bash
# Start GraphQL IDE
# from v2 add `--cors` to cross-origin resource sharing
$ openapi-to-graphql --cors -u http://localhost:8000/carbonster/v1/ openapi/carbonster-api.yaml
```

Open [index](html/index.html) on browser (YOUR/LOCAL/PATH/html/index.html)

## Database schema

### carbonIntensitytest

| Field Name           | Data Type   | Description |
| :------------------- | :---------- | :---------- |
| country              | varchar(20) | country code |
| carbonIntensity      | float       | carbon dioxide emission |
| fossilFuelPercentage | float       | fossil fuel percentage (didn't use) |
| datetime             | timestamp   | timestamp when getting data |

### carbontest

| Field Name | Data Type   | Description |
| :--------- | :---------- | :---------- |
| country    | varchar(20) | country code |
| carbon_avg | float       | carbon monoxide emission |
| start      | timestamp   | timestamp when at the start getting data |
| end        | timestamp   | timestamp when at end of getting data |

### carbonTHapi

| Field Name | Data Type   | Description |
| :--------- | :---------- | :---------- |
| district   | varchar(20) | district in Thailand |
| carbon     | float       | carbon monoxide emission |
| ts         | timestamp   | timestamp when getting data |

### mettest

| Field Name  | Data Type   | Description |
| :---------- | :---------- | :---------- |
| country     | varchar(20) | country code |
| methane_avg | float       | methane emission |
| start      | timestamp   | timestamp when at the start getting data |
| end        | timestamp   | timestamp when at end of getting data |

### methaneTHapi

| Field Name | Data Type   | Description |
| :--------- | :---------- | :---------- |
| district   | varchar(20) | district in Thailand |
| methane    | float       | methane emission |
| ts         | timestamp   | timestamp when getting data |

### ozonetest

| Field Name | Data Type   | Description |
| :--------- | :---------- | :---------- |
| country    | varchar(20) | country code |
| ozone_avg  | float       | ozone emission |
| start      | timestamp   | timestamp when at the start getting data |
| end        | timestamp   | timestamp when at end of getting data |

### ozoneTHapi

| Field Name | Data Type   | Description |
| :--------- | :---------- | :---------- |
| district   | varchar(20) | district in Thailand |
| ozone      | float       | ozone emission |
| ts         | timestamp   | timestamp when getting data |

### population

| Field Name | Data Type   | Description |
| :--------- | :---------- | :---------- |
| country    | varchar(20) | country code |
| population | int         | population of that country |
| year       | int         | year of data collection |

### code

| Field Name | Data Type   | Description |
| :--------- | :---------- | :---------- |
| country    | varchar(20) | country code |
| population | int         | population of that country |
| year       | int         | year of data collection |
