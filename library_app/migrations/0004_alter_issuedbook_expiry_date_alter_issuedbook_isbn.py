# Generated by Django 4.2.16 on 2024-10-21 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_alter_issuedbook_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 5, 17, 0, 57, 393965)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='isbn',
            field=models.CharField(max_length=30),
        ),
    ]
