# Generated by Django 3.2.12 on 2022-09-15 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskid',
            name='UniqueID',
        ),
    ]
