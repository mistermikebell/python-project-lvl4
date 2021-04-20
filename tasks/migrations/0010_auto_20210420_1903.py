# Generated by Django 3.1.7 on 2021-04-20 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0004_auto_20210409_2145'),
        ('tasks', '0009_auto_20210420_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='statuses.status', verbose_name='Status'),
        ),
    ]
