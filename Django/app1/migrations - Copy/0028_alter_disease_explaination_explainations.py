# Generated by Django 3.2.16 on 2022-12-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_rename_disease_detailed_disease_explaination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease_explaination',
            name='explainations',
            field=models.CharField(blank=True, max_length=1500),
        ),
    ]
