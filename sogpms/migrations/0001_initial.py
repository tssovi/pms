# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 23:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('branch_name', models.CharField(max_length=250)),
                ('info', models.CharField(max_length=350)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bank',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField()),
                ('payment_type', models.CharField(max_length=20)),
                ('cheque_number', models.CharField(max_length=50)),
                ('transaction_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('money_receipt_number', models.CharField(max_length=50)),
                ('deposite_date', models.DateTimeField()),
                ('attached_file', models.CharField(blank=True, max_length=550, null=True)),
                ('is_deposited', models.CharField(default='Yes', max_length=10)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cheque_of_bank', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_cheque_bank', to='sogpms.Bank')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_created_by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_customer', to='sogpms.Customer')),
                ('deposite_to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_deposit_account', to='sogpms.Account')),
                ('deposite_to_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_deposit_bank', to='sogpms.Bank')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_address', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=25, null=True)),
                ('user_avatar', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
