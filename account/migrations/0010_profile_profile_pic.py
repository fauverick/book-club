# Generated by Django 4.2.7 on 2023-11-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='images/'),
        ),
    ]
