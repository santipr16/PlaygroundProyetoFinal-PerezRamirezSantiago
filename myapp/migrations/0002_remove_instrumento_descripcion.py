# Generated by Django 4.2.4 on 2023-08-31 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='descripcion',
        ),
    ]