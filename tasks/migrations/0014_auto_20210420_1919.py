# Generated by Django 3.1.7 on 2021-04-20 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0006_auto_20210420_1907'),
        ('tasks', '0013_auto_20210420_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='statuses.status'),
        ),
    ]
