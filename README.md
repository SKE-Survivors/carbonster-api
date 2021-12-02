# Carbonster API

## Members
- 6210545475 Nutta Sittipongpanich
- 6210545505 Nanthakarn Limkool
- 6210545611 Sahadporn Charnlertlakha

SKE17 Kasetsart University

## Overview
[Presentation slide](https://drive.google.com/file/d/1EMJkDjNAFis8yuj9Y0cx9-7depBLH7OU/view?usp=sharing)

### Motivation
Air pollution has become a big issue all over the world and In class assignment about pm2.5 has become a motivation to research about carbon emission because it is a big factor of air quality measure too.

### Goal
To provide information about carbon emissions and gas in Thailand and global to determine air quality in different perspective than PM2.5.

### Feature
- Statistic of CO CH4 O3 in each country
- Air quailty
  - Average CO CH4 O3 volume of each country
  - Average CO CH4 O3 volume in Thailand provinces (Bangkok*, Narathiwat, Khon Kaen, Rayong, Chiang Mai) 
- Correlation between Carbon emissions and population of each country
- Carbon emission, CO, CH4, O3 of each country
- Carbon emission per person

Note: Bangkok* is the data collected from KidBright

## Requirements

### Libraries
* OpenAPI-to-GraphQL
* PyMySQL

### Tools
* Python 3.6++
* HTML CSS Javascript
* Chart js
* Plotly
* Node-RED
* KidBright 32 V1.5i
* MQ-5 sensor
* ADS1115
 
## Installation 

* Clone this github project/ download ZIP file

```bash
$ git clone https://github.com/SKE-survivors/carbonster-api.git
```

* Download `OpenAPI-to-GraphQL`

```bash
# [if not yet have it] install OpenAPI-to-GraphQL
$ npm install -g openapi-to-graphql-cli@2.5.0
```

* Download/add `openapi-generator-cli-4.3.1.jar` to the project and download required libraries

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
|country: text|carbonIntensity: float|fossilFuelPercentage|datetime: timestamp|
|---|---|---|---|

### carbontest
|country: text|carbon_avg: float|start: timestamp|end: timestamp|
|---|---|---|---|

### carbonTHapi
|district: text|carbon: float|ts: timestamp
|---|---|---|

### mettest
|country: text|methane_avg: float|start: timestamp|end: timestamp|
|---|---|---|---|

### methaneTHapi
|district: text|methane: float|ts: timestamp
|---|---|---|

### ozonetest
|country: text|ozone_avg: float|start: timestamp|end: timestamp|
|---|---|---|---|

### ozoneTHapi
|district: text|ozone: float|ts: timestamp
|---|---|---|

### population
|country: text|population: int|year: int
|---|---|---|

### code
|country: text|code: text|
|---|---|
