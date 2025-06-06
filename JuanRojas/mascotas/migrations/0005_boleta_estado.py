# Generated by Django 4.2.1 on 2023-07-06 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_alter_boleta_idcliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('procesando', 'Procesando Pedido'), ('enviado', 'Pedido Enviado'), ('entregado', 'Pedido Entregado')], default='procesando', max_length=20, verbose_name='Estado de pedido'),
        ),
    ]
