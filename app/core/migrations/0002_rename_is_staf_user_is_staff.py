# Generated by Django 3.2.16 on 2022-10-13 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_staf',
            new_name='is_staff',
        ),
    ]
