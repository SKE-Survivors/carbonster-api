# Carbonster API

## Overview
[Presentation slide](https://drive.google.com/file/d/1EMJkDjNAFis8yuj9Y0cx9-7depBLH7OU/view?usp=sharing)

### Motivation
Air pollution has become a big issue all over the world and In class assignment about pm2.5 has become a motivation to research about carbon emission because it is a big factor of air quality measure too.

### Goal
To provide information about carbon emissions and gas in Thailand and global to determine air quality in different perspective than pm2.5.

## Members

- 6210545475 Nutta Sittipongpanich
- 6210545505 Nanthakarn Limkool
- 6210545611 Sahadporn Charnlertlakha

SKE17 Kasetsart University

## Installation 

Clone this github project/ download ZIP file

```bash
# [if not yet have it] install OpenAPI-to-GraphQL
$ npm install -g openapi-to-graphql-cli@2.5.0
```

Download/add `openapi-generator-cli-4.3.1.jar` to the project

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

## Members

- 6210545475 Nutta Sittipongpanich
- 6210545505 Nanthakarn Limkool
- 6210545611 Sahadporn Charnlertlakha
