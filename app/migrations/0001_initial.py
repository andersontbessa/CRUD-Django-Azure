# Generated by Django 3.2.16 on 2022-11-04 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=50)),
                ('animalName', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=30)),
                ('updateOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]