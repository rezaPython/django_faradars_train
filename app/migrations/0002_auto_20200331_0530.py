# Generated by Django 3.0.4 on 2020-03-31 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='choice',
        ),
        migrations.DeleteModel(
            name='question',
        ),
    ]
