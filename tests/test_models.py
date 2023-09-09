import pytest

from django.test import TestCase
from django.urls import reverse

from django.core.exceptions import ValidationError
from django.db import connection
from app import settings
from contato.models import Contato
#import sys, os
#myPath = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, myPath + '/../')
#sys.path.insert(0, myPath + './../api/models.py')



#original_db_name = settings.DATABASES["default"]["NAME"]

#pytestmark = pytest.mark.django_db

#@pytest.mark.django_db
class ContatoTest(TestCase):
    
    
    def setUp(self):
        """ Test initialized Contato  """
        Contato.objects.create(nome="Lennon", telefone="556798956231", email="lennon@thebeatles.com" )
        Contato.objects.create(nome="Paul",  telefone="556798956232",  email="Paul@thebeatles.com")

    def test_contato_is_configured(self):
        """ Test Contato configure app """
        self.assertTrue('api' in settings.INSTALLED_APPS)
        self.assertTrue('auth.User' == settings.AUTH_USER_MODEL)

    # @pytest.mark.django_db
    # @pytest.fixture(autouse=True)
    # pytestmark = pytest.mark.django_db
    def test_contato_select_nome(self):
        """ Test Contato compare nome """
        Lennon = Contato.objects.get(nome="Lennon")
        Paul = Contato.objects.get(nome="Paul")
        self.assertEqual(Lennon.nome, 'Lennon')
        self.assertEqual(Paul.nome, 'Paul')
    
    def test_contato_select_telefone(self):
        """ Test Contato compare telefone """
        fone = Contato.objects.get(id=1)
        expected_object_fone = f'{fone.telefone}'
        self.assertEquals(expected_object_fone, '556798956231')

    def test_contato_select_first_name_label(self):
        """ Test Contato name label """
        author = Contato.objects.get(id=1)
        field_label = author._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_contato_create_count(self):
        """ Test Contato create and count object """             
        Contato.objects.create(
            nome="John",  
            telefone="556798956233",
            email="John@thebeatles.com",
        )
        self.assertTrue(Contato.objects.count() == 3)
    
    def test_contato_must_have_email(self): 
        """ Test Contato deve ter o email """ 
        
        p = Contato(nome="John",  
            telefone="556798956233",
            email="example@mail.com",)
        with self.assertRaises(ValidationError):
            p.full_clean()

    def test_contato_save_empty_list_contato(self):
        """ Test Contato save empty """ 
        #list_ = Contato.objects.create()
        item  = Contato(nome='' , telefone='', email='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()


    def create_contato(self, nome="Lennon", telefone="556798956231",  email="lennon@thebeatles.com"):
        return Contato.objects.create(nome=nome, telefone=telefone, email=email)

    def test_contato_creation(self):
        w = self.create_contato()
        self.assertTrue(isinstance(w, Contato))
        self.assertEqual(w.__unicode__(), w.nome)




#if __name__ == '__main__':
#    unittest.main()           