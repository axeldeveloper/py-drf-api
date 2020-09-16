from django.db import models

from django.urls import reverse

# Create your models here.

class Contato(models.Model):

    class Meta:
        db_table = 'contato'
        ordering = ['-id']
        #paginate_by = 10

    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('contato-detail', args=[str(self.id)])

    def __str__(self):
        return self.nome