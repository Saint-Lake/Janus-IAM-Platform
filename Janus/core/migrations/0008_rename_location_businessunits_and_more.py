# Generated by Django 4.0.10 on 2024-02-14 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_workers_company'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='location',
            new_name='businessUnits',
        ),
        migrations.RenameModel(
            old_name='businessUnit',
            new_name='companies',
        ),
        migrations.RenameModel(
            old_name='job',
            new_name='costCenters',
        ),
        migrations.RenameModel(
            old_name='company',
            new_name='deparments',
        ),
        migrations.RenameModel(
            old_name='deparment',
            new_name='jobs',
        ),
        migrations.RenameModel(
            old_name='costCenter',
            new_name='locations',
        ),
    ]