# Generated by Django 4.0.1 on 2022-12-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_invoice_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='description2',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts')], max_length=100, null=True),
        ),
    ]
