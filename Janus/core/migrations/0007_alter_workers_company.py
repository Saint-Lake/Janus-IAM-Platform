# Generated by Django 4.0.10 on 2024-02-14 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_businessunitname_businessunit_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
    ]