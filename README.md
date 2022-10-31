# mbd-service

## Requirements

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Tech stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic

The project has been implemented following [Hexagonal Architecture](https://medium.com/ssense-tech/hexagonal-architecture-there-are-always-two-sides-to-every-story-bc0780ed7d9c) concept.


## Usage

* Build application
    ```sh
    make build
    ```

* Start application
    ```sh
    make up
    ```

* Init database (**note**: this step is required when running app for the first time - make sure the database container `mbd-service-db-1` is up and running and run this command in separate terminal)
    ```sh
    make init_db
    ```

## Endpoints

[Swagger](https://swagger.io/tools/swagger-ui/) has been used to document API endpoints.
Each endpoint can be called and tested directly from the browser:
```
http://localhost:8008/docs
```