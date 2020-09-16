import unittest
from django.test import TestCase



from api.models import Contato

from django.urls import reverse
from django.test import Client
client = Client()

class ContatoTestCase(TestCase):
    
    def setUp(self):
        """ Test initialized Contato  """
        Contato.objects.create(nome="Lennon", telefone="556798956231", email="lennon@thebeatles.com" )
        Contato.objects.create(nome="Paul",  telefone="556798956232",  email="Paul@thebeatles.com")

    def test_contato_select_nome(self):
        """ Test Contato compare name """
        Lennon = Contato.objects.get(nome="Lennon")
        Paul = Contato.objects.get(nome="Paul")
        self.assertEqual(Lennon.nome, 'Lennon')
        self.assertEqual(Paul.nome, 'Paul')

    def test_contato_first_name_label(self):
        """ Test Contato name label """
        author = Contato.objects.get(id=1)
        field_label = author._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_contato_create(self):
        """ Test Contato create object """
        
        Contato.objects.create(
            nome="John",  
            telefone="556798956233",
            email="John@thebeatles.com",
        )
        self.assertTrue(Contato.objects.count() == 3)

    def test_contato_get_byid_url(self):
        """ Test Contato get by id """

        response = client.get('http://localhost:8000/contatos/3')

        self.assertEqual(response.status_code, 200)
  
    def test_contato_welcome(self):
        """ Test Contato welcome url """
        response = client.get(reverse('welcome') , {}, secure=True)
        # assert response.status_code == 200
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context[-1]['message'], "Welcome to the BookStore!")
        
        #self.assertEqual(response.content == "Welcome to the BookStore!")


    #def test_get_absolute_url(self):
    #    print("Method: test_get_absolute_url. ")
    #    contato = Contato.objects.get(id=1)
    #    self.assertEquals(contato.get_absolute_url(), '/contatos/1')