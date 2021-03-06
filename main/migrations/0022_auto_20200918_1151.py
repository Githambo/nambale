# Generated by Django 3.0.10 on 2020-09-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200910_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.TextField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_number',
            field=models.TextField(max_length=20, unique=True),
        ),
    ]
