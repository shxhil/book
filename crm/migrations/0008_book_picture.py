# Generated by Django 4.2.6 on 2023-11-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_remove_book_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
