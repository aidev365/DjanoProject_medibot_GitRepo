# Generated by Django 3.2.12 on 2022-10-19 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_overall_detail_dateandtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='general_doc_detail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('doctorname', models.CharField(blank=True, max_length=15)),
                ('dateandtime', models.CharField(blank=True, max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.basic')),
            ],
        ),
    ]
