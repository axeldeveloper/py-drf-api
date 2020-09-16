import unittest
from django.test import TestCase


# Create your tests here.

# ./manage.py test
# app.contato.tests.ContatoTestCase
# test_contato_create.test_contato_create

# ./manage.py test app.contato.tests


# Run the specified module
# ./manage.py test app.contato.tests  --verbosity 2

# Run the specified module
#./manage.py test app.contato.tests.test_models


# Run the specified class
#./manage.py test app.contato.tests.test_models.ContatoTestCase


# Run the specified method
# ./manage.py test app.contato.tests.test_models.ContatoTestCase.test_contato_select_nome


# urls
# http://localhost:8000/contatos/


class InicialTestCase(TestCase):

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

