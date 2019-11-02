# Generated by Django 2.2 on 2019-04-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190430_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='select',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Not Available'), (1, 'Available')], default=1),
        ),
    ]