# Generated by Django 4.2.5 on 2023-09-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hngapp', '0002_alter_person_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone_number',
        ),
    ]
