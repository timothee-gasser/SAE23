# Generated by Django 4.2.2 on 2023-06-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cat', models.CharField(max_length=100)),
                ('des', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_client', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('date_inscri', models.DateField()),
                ('adresse', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Commandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_commande', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prod', models.CharField(max_length=100)),
                ('date_per', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='prod')),
                ('marque', models.CharField(max_length=100)),
                ('auteur', models.CharField(max_length=100)),
            ],
        ),
    ]
