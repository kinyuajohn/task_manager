# Generated by Django 4.2.1 on 2023-06-29 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
