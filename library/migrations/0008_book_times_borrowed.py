# Generated by Django 3.2 on 2021-04-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='times_borrowed',
            field=models.IntegerField(default=0),
        ),
    ]
