# Generated by Django 3.2 on 2021-04-23 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_borrowedbook_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='renew',
            field=models.BooleanField(default=False),
        ),
    ]
