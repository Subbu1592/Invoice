# Generated by Django 4.0.1 on 2023-01-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_invoice_total_amount_in_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount_in_words',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
