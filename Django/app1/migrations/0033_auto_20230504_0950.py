# Generated by Django 3.2.16 on 2023-05-04 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_auto_20230504_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackdata',
            old_name='DiagnosticAccuracy',
            new_name='admin_staff',
        ),
        migrations.RenameField(
            model_name='feedbackdata',
            old_name='Likelihoodtorecommend',
            new_name='medical_staff',
        ),
        migrations.RenameField(
            model_name='feedbackdata',
            old_name='UserExperience',
            new_name='nursing_staff',
        ),
        migrations.AlterField(
            model_name='feedbackupdated',
            name='dateandtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 4, 9, 50, 1, 325976)),
        ),
    ]
