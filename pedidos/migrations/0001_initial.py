# Generated by Django 4.1.2 on 2023-03-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0002_alter_produtos_photo_do_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=150)),
                ('numero_da_mesa', models.IntegerField(blank=True)),
                ('nome_do_cliente', models.CharField(max_length=150)),
                ('data_do_pedido', models.DateTimeField(auto_now_add=True)),
                ('valor_da_compra', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('status_de_pagamento', models.CharField(choices=[('pago', 'Pago'), ('pendente', 'Pendente')], default='pendente', max_length=15)),
                ('pedidos', models.ManyToManyField(blank=True, related_name='pedidos', to='produtos.produtos')),
            ],
        ),
    ]
