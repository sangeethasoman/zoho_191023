# Generated by Django 4.2.6 on 2023-10-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0036_auto_20231018_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebills',
            name='bill_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchasebills',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
