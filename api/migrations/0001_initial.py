# Generated by Django 2.0.5 on 2018-05-21 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fair',
            fields=[
                ('id', models.CharField(max_length=8)),
                ('long', models.CharField(max_length=10)),
                ('lat', models.CharField(max_length=10)),
                ('setcens', models.CharField(max_length=15)),
                ('areap', models.CharField(max_length=13)),
                ('coddist', models.CharField(max_length=9)),
                ('distrito', models.CharField(max_length=18)),
                ('codsubpref', models.CharField(max_length=2)),
                ('subpref', models.CharField(max_length=25)),
                ('regiao5', models.CharField(max_length=6)),
                ('regiao8', models.CharField(max_length=7)),
                ('nome', models.CharField(max_length=30)),
                ('registro', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('logadouro', models.CharField(max_length=34)),
                ('numero', models.CharField(max_length=5)),
                ('bairro', models.CharField(max_length=20)),
                ('referencia', models.CharField(max_length=24)),
            ],
        ),
    ]
