# Generated by Django 4.2.7 on 2023-11-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_profile_about_me_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='media/'),
        ),
    ]
