# Generated by Django 3.2.6 on 2021-09-06 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earn', '0005_alter_quiz_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='id',
            new_name='id_number',
        ),
    ]
