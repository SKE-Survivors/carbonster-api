# Carbonster API

An API project for gas data using OpenAPI and Python.

## Installation

```bash
# [if not yet have it] install OpenAPI-to-GraphQL
$ npm install -g openapi-to-graphql-cli@2.5.0
```

download/add `openapi-generator-cli-4.3.1.jar` to the project

```bash
# generate,update /autogen
$ java -jar openapi-generator-cli-4.3.1.jar generate -i openapi/carbonster-api.yaml -o autogen -g python-flask

$ cd autogen
$ pip install -r requirements.txt

# start sever
$ python -m openapi_server
```

run [app.py](app.py)

testing: go to <http://localhost:8000/carbonster/v1/ui>

in another terminal

```bash
# Start GraphQL IDE
# from v2 add `--cors` to cross-origin resource sharing
$ openapi-to-graphql --cors -u http://localhost:8080/carbonster/v1/ openapi/carbonster-api.yaml
```

open [index](html/index.html) on browser

## Members

- 6210545475 Nutta Sittipongpanich
- 6210545505 Nanthakarn Limkool
- 6210545611 Sahadporn Charnlertlakha
