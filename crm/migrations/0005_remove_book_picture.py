# Generated by Django 4.2.6 on 2023-11-14 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_book_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='picture',
        ),
    ]
