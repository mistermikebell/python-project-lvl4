# Generated by Django 3.2.2 on 2021-06-02 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
