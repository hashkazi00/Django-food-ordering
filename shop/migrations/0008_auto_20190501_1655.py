# Generated by Django 2.2 on 2019-05-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_place_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]