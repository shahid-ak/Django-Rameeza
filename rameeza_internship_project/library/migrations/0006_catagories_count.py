# Generated by Django 3.1.2 on 2020-11-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20201124_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagories',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
