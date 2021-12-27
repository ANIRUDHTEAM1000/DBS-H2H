# Generated by Django 3.1.5 on 2021-12-19 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_info',
            fields=[
                ('account_key', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('account_open_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.CharField(max_length=100)),
                ('rel_key', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('rule_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('applied', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('transactionkey', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('transactionamount', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=100)),
                ('transactiondate', models.DateField()),
                ('acc_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.account_info')),
                ('transaction_origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_info',
            fields=[
                ('partykey', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('party_open_date', models.DateField()),
                ('resident_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.countries')),
            ],
        ),
        migrations.AddField(
            model_name='account_info',
            name='primary_partkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating.customer_info'),
        ),
    ]