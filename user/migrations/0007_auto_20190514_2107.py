# Generated by Django 2.1.7 on 2019-05-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='profiles', verbose_name='Profile Picture'),
        ),
    ]
