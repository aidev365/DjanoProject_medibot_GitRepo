# Generated by Django 3.2.16 on 2023-04-20 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_auto_20230420_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmidata',
            name='BMI',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bmidata',
            name='Height',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='bmidata',
            name='Weight',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackupdated',
            name='dateandtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 20, 7, 22, 37, 94622)),
        ),
    ]
