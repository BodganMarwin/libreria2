# Generated by Django 4.2.1 on 2023-05-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicidad', '0002_articulos_clientes_pedidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=8),
        ),
    ]
