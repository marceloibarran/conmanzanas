# Generated by Django 2.2.1 on 2019-06-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bienesyservicios',
            name='idbs',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idcat',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pais',
            name='idpais',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='idreg',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='idsubc',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipocambio',
            name='id_cambio',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
