# Generated by Django 3.0.6 on 2020-10-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201014_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_detail',
            name='birth_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
