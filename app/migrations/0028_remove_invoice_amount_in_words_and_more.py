# Generated by Django 4.0.1 on 2023-01-11 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_rename_cgst_no_invoice_customer_gst_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='amount_in_words',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='card_no',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='course_amount',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='payment_mode',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='total',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='transaction_id',
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('invoice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.invoice')),
                ('course_amount', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('amount_in_words', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_mode', models.CharField(blank=True, choices=[('card', 'card'), ('cash', 'cash')], max_length=100, null=True)),
                ('card_no', models.IntegerField(blank=True, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            bases=('app.invoice',),
        ),
    ]