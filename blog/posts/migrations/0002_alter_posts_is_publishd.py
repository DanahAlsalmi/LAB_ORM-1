# Generated by Django 4.2.7 on 2023-11-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='is_publishd',
            field=models.BooleanField(default=False),
        ),
    ]
