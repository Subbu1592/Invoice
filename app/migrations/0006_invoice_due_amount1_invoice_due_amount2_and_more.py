# Generated by Django 4.1.4 on 2022-12-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_invoice_date_alter_invoice_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='due_amount1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='due_amount2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='due_amount3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
