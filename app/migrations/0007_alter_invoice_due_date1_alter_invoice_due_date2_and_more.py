# Generated by Django 4.1.4 on 2022-12-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_invoice_due_amount1_invoice_due_amount2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date3',
            field=models.DateField(blank=True, null=True),
        ),
    ]