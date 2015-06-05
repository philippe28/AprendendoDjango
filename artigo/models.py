# -*- coding:utf8 -*-
from __future__ import unicode_literals
from django.db import models
 
class Artigo(models.Model):
    class Meta:
        verbose_name = 'artigo'
    titulo = models.CharField(max_length=100, verbose_name='tÃ­tulo')
    conteudo = models.TextField(verbose_name='conteÃºdo')
    publicacao = models.DateTimeField(verbose_name='publicaÃ§Ã£o')
