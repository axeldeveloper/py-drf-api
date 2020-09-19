

import unittest
from django.test import TestCase
from django.urls import reverse, resolve
from django.test import Client
from api.models import Contato
from rest_framework import routers
from app.contato import views as contato_views
from django.http import HttpRequest
from http import HTTPStatus

client = Client()


class UrlTest(TestCase):
    
    def setUp(self):
        """ Test initialized Contato  """
        Contato.objects.create(nome="Lennon", telefone="556798956231", email="lennon@thebeatles.com" )
        Contato.objects.create(nome="Paul",  telefone="556798956232",  email="Paul@thebeatles.com")
    
    #def test_contato_get_byid_url(self):
    #    """ Test Contato get by id """

        #response = client.get('http://localhost:8000/contatos/1')
        #response = client.get('/contatos/1')

        #self.assertEqual(response.status_code, 200)
        #print("status :  ", response.status_code)
        #assert response.status_code == 200
  
    def test_contato_welcome(self):
        """ Test Contato welcome url """
        #response = client.get(reverse('welcome') , {}, secure=True)
        response = client.get(reverse('welcome') )
        # assert response.status_code == 301
        assert response.status_code == 200
        # self.assertEqual(response.content == "Welcome to the BookStore!")
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context[-1]['message'], "Welcome to the BookStore!")
           
    def test_get_absolute_url(self):
        """ Test Contato get_absolute_url. """
        contato = Contato.objects.get(id=1)
        self.assertEquals(contato.get_absolute_url(), '/contatos/1/')
  
    def test_home_page_returns_correct_html(self):
        """ Test Page Home html context  """
        request = HttpRequest()  
        response = contato_views.home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>To-Do lists</title>', html)  
        # self.assertTrue(html.endswith('</html>'))  

    def test_root_url_resolves_to_api(self):
        """ Test Page Home API  """
        found = resolve('/')  
        self.assertEqual(found.func.cls, routers.APIRootView)

    

    def test_resolution_for_foo(self):
        #resolver = resolve('/welcome')
        response = self.client.get('/welcome')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'message': 'Welcome to the BookStore!'}
        )

    def test_get_api_json(self):
        resp = self.api_client.get('/api/whatever/', format='json')
        self.assertValidJSONResponse(resp)
    
    def test_title_starting_lowercase(self):
        response = self.client.post(
            "/books/add/", data={"title": "a lowercase title"}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response, "Should start with an uppercase letter", html=True
        )

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = "You can't have an empty list item"
        self.assertContains(response, expected_error)