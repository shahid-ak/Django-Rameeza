# Generated by Django 3.1.2 on 2020-11-24 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20201124_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='discrption',
            new_name='discription',
        ),
    ]
