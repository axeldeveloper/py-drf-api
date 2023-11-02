# Project  - Django REST API

    Django
    Django Rest
    sqlite
    python 3.8 or 3.11


# Create project local
```sh 
$ python -m venv ven311
$ source ven311/bin/activate
$ pip install -r requirements.txt

```
# Dependencies
    pipenv
    Django
    pip install djangorestframework


## Using pyenv
    pyenv shell 3.8.17



## Install Django and Django REST framework into the virtual environment

$ pipenv install django

$ pipenv install djangorestframework

$ pipenv install pytest



# Set up a new project with a single application

```sh 
# project
$ django-admin startproject app .  # Note the trailing '.' character
# app
$ django-admin startapp contato
$ cd ..
# sync your database for the first time:
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser --email axelpatton@gmail.com --username axel
$ python manage.py migrate --fake core zero
$ python manage.py showmigrations
$ python manage.py migrate --fake-initial
```

# Run and teste
```sh
# run
$ python manage.py runserver

# run set setting
$ python DJANGO_SETTINGS_MODULE=<your_app_name>.settings_dev python manage.py runserver 

. .env

$ python manage.py makemigrations --settings=djangoproject.settings.development

$ python manage.py migrate --settings=djangoproject.settings.developmen
```

# Activate virtual environment

    pipenv shell
    source /home/axel/.local/share/virtualenvs/app-drf-api-g3fTGEph/bin/activate


# Test TDD

## Create your folder tests here.
```sh
$ py.test -v          `or`
$ pytest -v           `or`
$ pytest -m slow      `or`
$ py.test -q ./api/test_example.py
$ pytest ./api/test_example.py -v
$ pipenv run pytest   `or`

$ ./manage.py test tests.test_models.ContatoTest  --verbosity 2
--verbosity 2
$ ./manage.py test tests.test_models --verbosity 2
$ ./manage.py test tests.test_models.ContatoTest.test_contato_select_nome
$ ./manage.py test app.contato.tests.test_models.ContatoTest

$ PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider

$ ./manage.py test tests.test_url.UrlTest  
$ coverage run --source='.' ./manage.py test tests.test_url.UrlTest --verbosity 2
$ coverage run  ./manage.py test tests.test_url.UrlTest
```


# urls

https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
