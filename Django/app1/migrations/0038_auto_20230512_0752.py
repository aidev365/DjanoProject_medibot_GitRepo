# Generated by Django 3.2.16 on 2023-05-12 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_auto_20230512_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdata',
            name='fromwhichsite',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackupdated',
            name='dateandtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 7, 52, 13, 491316)),
        ),
    ]
