# Generated by Django 3.2.20 on 2023-10-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0027_repeat_everyterms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor_table',
            old_name='bpin',
            new_name='battention',
        ),
        migrations.RenameField(
            model_name='vendor_table',
            old_name='bstreet',
            new_name='bzip',
        ),
        migrations.RenameField(
            model_name='vendor_table',
            old_name='spin',
            new_name='sattention',
        ),
        migrations.RenameField(
            model_name='vendor_table',
            old_name='sstreet',
            new_name='szip',
        ),
        migrations.AddField(
            model_name='vendor_table',
            name='opening_bal_type',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor_table',
            name='status',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='company_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='currency',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='department',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='designation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='gst_number',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='gst_treatment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='opening_bal',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='pan_number',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='payment_terms',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='salutation',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='skype_number',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='source_supply',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='vendor_display_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='vendor_email',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='vendor_mphone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='vendor_wphone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor_table',
            name='website',
            field=models.CharField(default='', max_length=250),
        ),
    ]