# Generated by Django 4.0.1 on 2023-01-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_receipt_for_the_course_of2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='description',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='description2',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='description3',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts')], max_length=100, null=True),
        ),
    ]
