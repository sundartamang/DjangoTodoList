# Generated by Django 2.2.4 on 2020-07-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is completed ?'),
        ),
    ]
