# Generated by Django 2.2.3 on 2019-07-14 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='status',
            new_name='done',
        ),
    ]
