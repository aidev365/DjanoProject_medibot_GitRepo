# Generated by Django 3.2.16 on 2023-03-29 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_feedbackupdated_dateandtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdffile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueis', models.CharField(blank=True, max_length=1500)),
                ('filedata', models.FileField(upload_to='images/')),
                ('dateandtime', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='whatsappdata',
            name='uniqueis',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='feedbackupdated',
            name='dateandtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 29, 3, 13, 55, 165244)),
        ),
    ]
