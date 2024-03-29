# Generated by Django 4.0.10 on 2024-02-14 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_businessunitcode_workers_businessunit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='businessUnit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.businessunit'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='costCenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.costcenter'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.deparment'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='jobTitle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.job'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.location'),
        ),
    ]
