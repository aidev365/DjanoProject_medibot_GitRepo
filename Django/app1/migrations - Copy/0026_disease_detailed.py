# Generated by Django 3.2.16 on 2022-12-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_diagnosis_diet_image_id_risk_factors_skin_image_symptom_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease_detailed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseasename', models.CharField(blank=True, max_length=15)),
                ('detailedname', models.CharField(blank=True, max_length=500)),
                ('explainations', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
