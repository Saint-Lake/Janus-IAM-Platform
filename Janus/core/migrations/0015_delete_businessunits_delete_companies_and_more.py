# Generated by Django 4.0.10 on 2024-02-16 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_delete_jobs_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='businessUnits',
        ),
        migrations.DeleteModel(
            name='companies',
        ),
        migrations.DeleteModel(
            name='costCenters',
        ),
        migrations.DeleteModel(
            name='departments',
        ),
        migrations.DeleteModel(
            name='locations',
        ),
        migrations.DeleteModel(
            name='title',
        ),
        migrations.CreateModel(
            name='businessUnits',
            fields=[
                ('commoncodelistfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commoncodelistfields')),
            ],
            bases=('core.commoncodelistfields',),
        ),
        migrations.CreateModel(
            name='companies',
            fields=[
                ('commoncodelistfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commoncodelistfields')),
            ],
            bases=('core.commoncodelistfields',),
        ),
        migrations.CreateModel(
            name='costCenters',
            fields=[
                ('commoncodelistfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commoncodelistfields')),
            ],
            bases=('core.commoncodelistfields',),
        ),
        migrations.CreateModel(
            name='departments',
            fields=[
                ('commoncodelistfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commoncodelistfields')),
            ],
            bases=('core.commoncodelistfields',),
        ),
        migrations.CreateModel(
            name='locations',
            fields=[
                ('commoncodelistfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commoncodelistfields')),
            ],
            bases=('core.commoncodelistfields',),
        ),
        migrations.CreateModel(
            name='title',
            fields=[
                ('commoncodelistfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.commoncodelistfields')),
            ],
            bases=('core.commoncodelistfields',),
        ),
        migrations.AlterField(
            model_name='Workers',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.companies'),
        ),
    ]
