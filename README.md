# Fampay-Backend-Assignment

## Introduction:
This backend assignment is made in django-rest-framework on postgresql database with periodinc tasks running on celery beat and redis. \
I have setup a celery beact with redis running every 10 minutes for asynchronous task scheduling, with docker compose.

## API Documentation
1) Listing api of youtube fetched data works on get request giving paginated reponse \  
Endpoint: ```http://localhost:1337/api/youtube/list```

2) Searching api will return response of video data based on title and description given in query param. For fuzzy search I have used TrigramSimilarity querying given by postgresql for search.
Endpoint: ```http://localhost:1337/api/youtube/search?title=python``` \
Endpoint: ```http://localhost:1337/api/youtube/search?description=write description here```

## Run this project with docker or in localhost as below:
### Dont forget to update your youtube apikey and django secret
```
$ docker-compose -f docker-compose.prod.yml up -d --build 
``` 

Server will start at ``` http://localhost:1337/ ``` 

Thank YOU!
 


