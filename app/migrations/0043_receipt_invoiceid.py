# Generated by Django 3.0.5 on 2023-01-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_delete_invoiced_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='InvoiceId',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]