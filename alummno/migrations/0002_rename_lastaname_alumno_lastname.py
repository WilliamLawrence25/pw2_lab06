# Generated by Django 5.0.6 on 2024-05-29 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alummno', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='lastaname',
            new_name='lastname',
        ),
    ]