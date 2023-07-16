# DjangoREST Social Network 

### Create and activate virtual environment
`python3 -m venv venv`

`source venv/bin/activate`

### Install the required pip packages
make sure you are in project folder

`pip install -r requirements.txt`

### Migrate the database
make sure you are in project folder

`python manage.py makemigrations`

`python manage.py migrate`

### Don't forget to run the unit test
`pytest -v`

### Run the server and enjoy
`python manage.py runserver`

### Swagger API gateway
`http://127.0.0.1:8000/swagger/`

### API documentation 
`http://127.0.0.1:8000/redoc/`

### Deploy on docker (to be continued)
``