# Generated by Django 3.1.2 on 2020-11-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='img',
            field=models.ImageField(upload_to='book'),
        ),
    ]