# Generated by Django 5.0.4 on 2024-04-16 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]
