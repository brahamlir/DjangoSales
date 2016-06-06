# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-31 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20160526_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescripcionVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50)),
                ('cantidad', models.FloatField(default=0)),
                ('precio_unitario', models.FloatField(default=0)),
            ],
            options={
                'verbose_name_plural': 'DescripcionVentas',
                'verbose_name': 'DescripcionVenta',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('usuario', models.CharField(max_length=50)),
                ('total_compra', models.FloatField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Ventas',
                'verbose_name': 'Venta',
            },
        ),
        migrations.AlterModelOptions(
            name='catalogocategoria',
            options={'verbose_name': 'CatalogoCategoria', 'verbose_name_plural': 'Catalogo Categorias'},
        ),
        migrations.AlterModelOptions(
            name='entradas',
            options={'verbose_name': ' Entradas', 'verbose_name_plural': 'Entradas'},
        ),
        migrations.AddField(
            model_name='entradas',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='administrador.CatalogoCategoria'),
        ),
        migrations.AddField(
            model_name='descripcionventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Venta'),
        ),
    ]