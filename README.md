# Backend Challenge

This is a FastAPI application that manages a database of shells.

## Getting Started

This application uses docker, so insure that docker can be run on your system. 

Run the following command to start the app

```
docker compose up --build
```

This will start the application running at localhost:8000

## Endpoints

Documentation can be accessed at the following location:

localhost:8000/docs/

A new shell can be created at this endpoint:

localhost:8000/api/v1/shells/

All shells can be retrieved from this endpoint with optional query parameters to return a certain range:

localhost:8000/api/v1/shells/

A specific shell can be retrieved from this endpoint:

localhost:8000/api/v1/shells/{shell_id}

A specific shell can be updated from this endpoint:

localhost:8000/api/v1/shells/{shell_id}

A specific shell can be deleted from this endpoint:

localhost:8000/api/v1/shells/{shell_id}

Please see documentation for specific requirements.

## Shutting Down

When finished, the application can be cleaned up using the following command:

```
docker compose down
```


