# Generated by Django 3.1.7 on 2021-04-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0005_auto_20210420_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(max_length=200),
        ),
    ]