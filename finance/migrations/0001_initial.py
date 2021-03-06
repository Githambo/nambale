# Generated by Django 3.0.10 on 2020-09-14 18:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0021_auto_20200910_2209'),
        ('corecode', '0004_expensecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_from_previous_term', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], default='active', max_length=20)),
                ('class_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.StudentClass')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.AcademicSession')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.AcademicTerm')),
            ],
            options={
                'ordering': ['student', 'term'],
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField()),
                ('date_paid', models.DateField(default=django.utils.timezone.now)),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_incurred', models.DateField(default=datetime.date.today)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.ExpenseCategory')),
            ],
        ),
    ]
