# Generated by Django 4.0.10 on 2024-02-14 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_workers_businessunit_alter_workers_costcenter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workers',
            name='businessUnit',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='costCenter',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='department',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='jobTitle',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='location',
        ),
    ]