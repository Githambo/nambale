# Generated by Django 3.0.10 on 2020-09-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0003_auto_20200726_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]