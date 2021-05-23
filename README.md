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
    > DJANGO_SETTINGS_MODULE=<your_app_name>.settings_dev python3 manage.py runserver

    . .env
    ./manage.py makemigrations --settings=djangoproject.settings.development
    ./manage.py migrate --settings=djangoproject.settings.developmen

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

## Create your folder tests here.

    $ py.test -v          `or`
    $ pytest -v           `or`
    $ pytest -m slow      `or`
    $ py.test -q ./api/test_example.py
    $ pytest ./api/test_example.py -v
    $ pipenv run pytest   `or`
    $ ./manage.py test tests.test_models.ContatoTest  --verbosity 2
    $ ./manage.py test tests.test_models --verbosity 2
    $ ./manage.py test tests.test_models.ContatoTest.test_contato_select_nome
    $ ./manage.py test app.contato.tests.test_models.ContatoTest
    $ PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider
    $ pipenv run pytest --ds=app.test_settings
    $ ./manage.py test tests.test_url.UrlTest --verbosity 2
    $ coverage run --source='.' ./manage.py test tests.test_url.UrlTest --verbosity 2
    $ coverage run  ./manage.py test tests.test_url.UrlTest

# urls

# http://localhost:8000/contatos/

https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
