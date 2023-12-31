# Generated by Django 3.2.20 on 2023-10-18 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0035_auto_20231017_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='adjust',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='advance',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='cheque_id',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='complete_status',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='pay_method',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='upi_id',
        ),
        migrations.AddField(
            model_name='estimateitems',
            name='hsn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='estimates',
            name='convert_invoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='estimates',
            name='convert_sales',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='estimates',
            name='customer_mailid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='estimates',
            name='customer_placesupply',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zohoapp.bankcreation'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='estimate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI'), ('bank', 'Bank')], default='cash', max_length=50),
        ),
        migrations.AddField(
            model_name='invoice_item',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice_item',
            name='paid_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='retainerinvoice',
            name='balance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='retainerinvoice',
            name='customer_mailid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='retainerinvoice',
            name='customer_name1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='retainerinvoice',
            name='customer_placesupply',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='estimate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='setting_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(blank=True, max_length=25, null=True)),
                ('pricelist', models.CharField(blank=True, max_length=25, null=True)),
                ('offline_banking', models.CharField(blank=True, max_length=25, null=True)),
                ('banking', models.CharField(blank=True, max_length=25, null=True)),
                ('customers', models.CharField(blank=True, max_length=25, null=True)),
                ('estimates', models.CharField(blank=True, max_length=25, null=True)),
                ('retainer_invoices', models.CharField(blank=True, max_length=25, null=True)),
                ('sales_orders', models.CharField(blank=True, max_length=25, null=True)),
                ('delivery_challans', models.CharField(blank=True, max_length=25, null=True)),
                ('invoices', models.CharField(blank=True, max_length=25, null=True)),
                ('credit_notes', models.CharField(blank=True, max_length=25, null=True)),
                ('recurring_invoices', models.CharField(blank=True, max_length=25, null=True)),
                ('vendors', models.CharField(blank=True, max_length=25, null=True)),
                ('vendor_credits', models.CharField(blank=True, max_length=25, null=True)),
                ('expenses', models.CharField(blank=True, max_length=25, null=True)),
                ('recurring_expenses', models.CharField(blank=True, max_length=25, null=True)),
                ('purchase_orders', models.CharField(blank=True, max_length=25, null=True)),
                ('payment_made', models.CharField(blank=True, max_length=25, null=True)),
                ('bills', models.CharField(blank=True, max_length=25, null=True)),
                ('recurring_bills', models.CharField(blank=True, max_length=25, null=True)),
                ('projects', models.CharField(blank=True, max_length=25, null=True)),
                ('chart_of_accounts', models.CharField(blank=True, max_length=25, null=True)),
                ('employees', models.CharField(blank=True, max_length=25, null=True)),
                ('employees_loan', models.CharField(blank=True, max_length=25, null=True)),
                ('pdf', models.CharField(blank=True, max_length=25, null=True)),
                ('slip', models.CharField(blank=True, max_length=25, null=True)),
                ('print_opt', models.CharField(blank=True, max_length=25, null=True)),
                ('user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='retainer_payment_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_opt', models.CharField(blank=True, max_length=100, null=True)),
                ('acc_no', models.CharField(blank=True, max_length=100, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zohoapp.bankcreation')),
                ('retainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.retainerinvoice')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
