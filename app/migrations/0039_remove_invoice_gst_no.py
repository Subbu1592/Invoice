# Generated by Django 3.0.5 on 2023-01-20 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20230119_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='gst_no',
        ),
    ]