# Generated by Django 2.1 on 2018-08-10 20:20

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacao', '0002_auto_20180810_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('autenticacao.user',),
        ),
    ]
