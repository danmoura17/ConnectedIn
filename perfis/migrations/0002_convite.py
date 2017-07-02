# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('convidado', models.ForeignKey(related_name='convites_recebidos', to='perfis.Perfil')),
                ('solicitante', models.ForeignKey(related_name='convites_feitos', to='perfis.Perfil')),
            ],
        ),
    ]
