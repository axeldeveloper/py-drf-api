from django.db import models

from django.urls import reverse

from django.core.exceptions  import ValidationError

class Contato(models.Model):

    class Meta:
        db_table = 'contato'
        ordering = ['-id']
        #paginate_by = 10

    nome     = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=200)
    email    = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('contato-detail', args=[str(self.id)])

    def clean(self):
        # and self.website is None
        
        if self.nome == None and self.nome == "":
            raise ValidationError({
                'nome': "Nome obrigatório"
            })
        
        if self.email == 'example@mail.com' :
            raise ValidationError({
                'email': "E-mail invalido"
            })

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome