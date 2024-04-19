# FastAPI User Management API

## Synopsis

This application provides a RESTful API for user management, utilizing FastAPI with SQLite for data persistence. It supports operations such as creating, reading, updating, and deleting user information. The API is documented and can be interacted with via Swagger UI and ReDoc.

## Minimum Python Version

- Python 3.7 or higher

## Installation

Install the required dependencies using pip:

``` pip install -r requirements.txt ```


## Starting the API

Launch the API server with the following command:

``` ./start_service.sh ```

or on Windows

``` start_service.bat ```


The `--reload` option is recommended during development for automatic reloading on code changes but can be removed for production.

## Accessing API Documentation

- **Swagger UI**: Interact with the API by visiting [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
- **ReDoc**: View the API documentation at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).
