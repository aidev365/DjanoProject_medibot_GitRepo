# Generated by Django 3.2.12 on 2022-10-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_special_doc_detail_recevingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='special_doc_detail',
            name='module_name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]