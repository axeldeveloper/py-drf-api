from http import HTTPStatus
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import resolve, reverse
from rest_framework import routers
from contato.models import Contato
from contato.views import home_page

client = Client()

class UrlTest(TestCase):
    
    def setUp(self):
        """ Test initialized Contato  """
        Contato.objects.create(nome="Lennon", telefone="556798956231", email="lennon@thebeatles.com" )
        Contato.objects.create(nome="Paul",  telefone="556798956232",  email="Paul@thebeatles.com")
    
    def test_home_page_context_html(self):
        """ TEST PAGE HOME CONTEXT HTML """
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>Minha Pagina</title>', html)  
        self.assertTrue(html.endswith('</html>'))  

    def test_root_url_api(self):
        """ TEST ROOT API ROOTVIEW """
        found = resolve('/')  
        self.assertEqual(found.func.cls, routers.APIRootView)

    def test_get_absolute_url(self):
        """ TEST GET CONTATO GET_ABSOLUTE_URL. """
        contato = Contato.objects.get(id=1)
        self.assertEquals(contato.get_absolute_url(), '/contatos/1/')
    
    def test_get_status_for_welcome(self):
        """ TEST GET STATUS WELCOME URL """
        #response = client.get(reverse('welcome') , {}, secure=True)
        response = client.get(reverse('welcome') )
        assert response.status_code == HTTPStatus.OK 
        
    def test_get_json_for_welcome(self):
        """ TEST PAGE WELCOME JSON """
        url = reverse('welcome')
        response = self.client.get(url)    
        #self.assertEqual(response.status_code, HTTPStatus.OK)   
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'message': 'Welcome to the DRF!'}
        )

    def test_get_json_for_foo(self):
        """ TEST PAGE FOO JSON """
        response = client.get('/foo/',  format='json')
        assert response.status_code == HTTPStatus.OK
 
    
    #def test_title_starting_lowercase(self):
    #    response = self.client.post(
    #        "/books/add/", data={"title": "a lowercase title"}
    #    )
    #
    #    self.assertEqual(response.status_code, HTTPStatus.OK)
    #    self.assertContains(
    #        response, "Should start with an uppercase letter", html=True
    #    )

    #def test_validation_errors_are_sent_back_to_home_page_template(self):
    #    response = self.client.post('/lists/new', data={'item_text': ''})
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, 'home.html')
    #    expected_error = "You can't have an empty list item"
    #    self.assertContains(response, expected_error)


     #def test_contato_get_byid_url(self):
    #    """ Test Contato get by id """

        #response = client.get('http://localhost:8000/contatos/1')
        #response = client.get('/contatos/1')

        #self.assertEqual(response.status_code, 200)
        #print("status :  ", response.status_code)
        #assert response.status_code == 200
  
