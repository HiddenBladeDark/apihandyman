# Generated by Django 3.1.2 on 2020-10-09 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportService', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]