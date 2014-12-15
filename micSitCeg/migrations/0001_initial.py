# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interesados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('extension', models.CharField(max_length=10)),
                ('celular', models.CharField(max_length=10)),
                ('insertDate', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
