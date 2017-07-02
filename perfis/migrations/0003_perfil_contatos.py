# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='contatos',
            field=models.ManyToManyField(to='perfis.Perfil', related_name='_contatos_+'),
        ),
    ]
