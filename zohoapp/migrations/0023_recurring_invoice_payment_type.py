# Generated by Django 3.2.20 on 2023-10-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0022_auto_20231003_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_invoice',
            name='payment_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
