# Generated by Django 2.2 on 2019-04-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
