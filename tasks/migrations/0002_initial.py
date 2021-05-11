# Generated by Django 3.2.2 on 2021-05-11 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0001_initial'),
        ('statuses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks_executor', to='users.usermodel', verbose_name='Executor'),
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.LabelsTask', to='labels.Label', verbose_name='Labels'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='statuses.status', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='labelstask',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='labels.label'),
        ),
        migrations.AddField(
            model_name='labelstask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
