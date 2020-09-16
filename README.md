# Create Project 

    mkdir app-drf-api
    cd app-drf-api


# Install Django and Django REST framework into the virtual environment

    $ pipenv install django
    $ pipenv install djangorestframework
    $ pipenv install pytest


# Set up a new project with a single application

    > django-admin startproject app .  # Note the trailing '.' character
    > cd app
    > django-admin startapp contato
    > cd ..


# Now sync your database for the first time:

    $ python manage.py makemigrations    
    $ python manage.py migrate
    $ python manage.py createsuperuser --email axel@gmail.com --username axel    
    $ python manage.py showmigrations


# Clear the migration history (please note that contato is the name of my app):
    $ python manage.py migrate --fake core zero
    $ python manage.py showmigrations

    `Remove the actual migration files`
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete

    $ python manage.py showmigrations
    $ python manage.py makemigrations
    $ python manage.py migrate --fake-initial


# Run and teste

    > python manage.py runserver

# Dependencies 

    pipenv
    Django
    pip install djangorestframework

# out after pipenv shell 
    ✔ Successfully created virtual environment!
    Virtualenv location: /home/axel/.local/share/virtualenvs/app-drf-api-g3fTGEph
    Creating a Pipfile for this project…
    Launching subshell in virtual environment…
    . /home/axel/.local/share/virtualenvs/app-drf-api-g3fTGEph/bin/activate



# Activate virtual environment
    pipenv shell
    source /home/axel/.local/share/virtualenvs/app-drf-api-g3fTGEph/bin/activate


# test TDD 