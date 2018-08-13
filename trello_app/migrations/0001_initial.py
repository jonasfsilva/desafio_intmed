# Generated by Django 2.1 on 2018-08-13 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loja', '0002_auto_20180810_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trello_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CardPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trello_app.Card')),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loja.Pedido')),
            ],
        ),
    ]