# Generated by Django 3.2.7 on 2022-01-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idMeal', models.IntegerField()),
                ('strMeal', models.CharField(max_length=255)),
                ('strCategory', models.CharField(max_length=255)),
                ('strArea', models.CharField(max_length=255)),
                ('strInstructions', models.TextField()),
            ],
        ),
    ]
