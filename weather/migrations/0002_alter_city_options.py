# Generated by Django 4.0.3 on 2022-04-04 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['cityName']},
        ),
    ]