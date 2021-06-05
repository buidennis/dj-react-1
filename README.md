Django REST with React

Application Specifications:
    Lead
        Fields
            & Name
            & Email
            & Message
            & DateCreate

python3 -m venv venv
source venv/bin/active

1. Create new application in Django
    django-admin startapp app_name
    
    e.g:
        django-admin startapp leads
        Create new leads app in django-react folder
Current Project Structure:

|-- django_react
|
|-- leads
|
|-- venv

2. Creating a Django model

    Model is an object representing a table's data
        & One or many fields
        & Each field is a column in the table

    leads/models.py

    python manage.py makemigrations leads

3. Django REST with React: Testing

    & not Django built-in code [models, views, etc]
    & not Python built-in functions

    & are testing custom methods in Django model

    pip install coverage
    coverage html
    coverage report

4. Django REST Serializers

    Serialization:
        & Act of transforming an object into another data format
        & After transforming save it to a file and send through network

    Why:
        & Django Model == Python Class
        & Render a Python class to JSON || JSON to Objects
        & Display Django models in a browser via converting to JSON
        & Make CRUD request with JSON payload to the API

    leads/serializer.py

5. Setting Up Controls ~ Views

    Django ~ Model View Template Framework

    Views:
        & Function Based View
        & Class Based View
        && Generic API View

   ~ Function views only iff time spent customizing generic view is more than time spent writing by hand 

   & List a collection of models
   & Create new objects in the database

   Generic API Views
       & ListCreateAPIView 
            & Takes in Queryset && Serializer_Class

6. Setting Up Routing ~ URLs

   Link LeadListCreate to api/lead/ 
        & tldr: GET and POST requests to api/lead/ for listing and creating models

    lead/urls.py
    api/leads/
        & add leads api path
    django_react/settings.py
        & enable rest_framework in INSTALLED_APPS

7. Django and React

   A. (Medium)
       Django:
           Load in a single HTML template
       React:
           Manage the Front End 
       & Building web based app 
       & Interface has a lot of user interactions/AJAX 
       & Session based authentification
       & No SEO concerns
       & Okay with React Router

   B. (Hard)
       Django REST:
           Standalone API
       React: 
           Standalone SPA 

8. React and Webpack
    
django-admin startapp frontend

|
|-- django-react
|
|-- frontend
|
|-- leads
|
|-- venv

React Components
    mkdir -p ./frontend/src/components

Static Files
    mkdir -p ./frontend/{static,templates}/frontend

React, webpack, and babel
    & Move into the front end folder
    & Initialize the environment
    cd ./frontend && npm init -y

Install Webpack and Webpack Cli
    npm i webpack webpack-cli --save-dev

package.json
    "scripts": {
        "dev": "webpack --mode development --entry ./src/index.js --output-path ./static/frontend",
        "build": "webpack --mode production --entry ./src/index.js --output-path ./static/frontend"
    },

install babel for transpilling code:
    npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev

pull in React
    npm i react react-dom --save-dev

configure babel [./frontend/.babelrc]
    {
        "presets": [
            "@babel/preset-env", "@babel/preset-react"
        ]
    }

9. Django REST With React: Preparing The Frontend App
./frontend/views.py:

    from django.shortcuts import render

    def index(request):
    return render(request, 'frontend/index.html')

./frontend/templates/frontend/index.html

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Django REST with React</title>
</head>
<body>
<div id="app">
    <!-- React will load here -->
</div>
</body>
{% load static %}
<script src="{% static "frontend/main.js" %}"></script>
</html>

Source Material:
    & https://www.valentinog.com/blog/drf/
