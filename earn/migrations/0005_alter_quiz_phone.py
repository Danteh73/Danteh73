# Generated by Django 3.2.6 on 2021-09-06 13:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('earn', '0004_alter_quiz_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
