from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def _str_(self):
        return self.nome

