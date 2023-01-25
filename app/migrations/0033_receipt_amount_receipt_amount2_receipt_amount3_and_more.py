# Generated by Django 4.0.1 on 2023-01-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_receipt_description_receipt_description2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='amount2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='amount3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='quantity2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='quantity3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='unit_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='unit_price2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='unit_price3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
