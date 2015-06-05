# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='t\xc3\xadtulo')),
                ('conteudo', models.TextField(verbose_name='conte\xc3\xbado')),
                ('publicacao', models.DateTimeField(verbose_name='publica\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'verbose_name': 'artigo',
            },
        ),
    ]
