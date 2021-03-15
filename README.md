# django-auth-api
Django API for users authentication using the Django REST Framework.


Project still in development

## Project setup

For compiling this project make sure you have [Docker](https://www.docker.com) installed. It will setup automatically a container image with all the dependencies needed to execute our Django API.

We will be using the port 8000 for running our Django API so make sure you don't have any service already running in that port.

For changing the default configurations feel free to overwrite the files `Dockerfile` and `docker-compose.yml`.

### Steps

1. Download the source code and open a terminal it's main folder.

2. Start the [Docker](https://www.docker.com) desktop application.

3. Run the command `docker-compose up` in the terminal to install all the dependencies into the docker container.

3. Make sure you don't have any errors and the Django app is running in the [localhost:8000](http://localhost:8000).

4. Login with the administrator account which is already defined with username and password as `admin`.

5. Access the Users API at the [localhost:8000/users/](http://localhost:8000/users) endpoint.


