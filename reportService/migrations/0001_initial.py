# Generated by Django 3.1.2 on 2020-10-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTecni', models.CharField(blank=True, max_length=255, null=True)),
                ('idServi', models.CharField(blank=True, max_length=255, null=True)),
                ('datStart', models.DateTimeField(blank=True, null=True)),
                ('datEnd', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
