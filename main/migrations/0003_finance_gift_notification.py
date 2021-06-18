# Generated by Django 3.1 on 2020-09-05 14:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200905_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(choices=[('Abuse', 'Abuse'), ('Health', 'Health'), ('Location', 'Location')], null=True)),
                ('notification_date', models.DateField(default=datetime.date.today)),
                ('detail', models.TextField(choices=[('sick', 'sick'), ('admitted', 'admitted'), ('accident', 'accident'), ('raped', 'raped'), ('missing', 'missing'), ('assaulted', 'assaulted')], null=True)),
                ('status', models.TextField(choices=[('not_collected', 'not_collected'), ('collected', 'collected')], default='not_collected')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_type', models.TextField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.IntegerField()),
                ('date_of_contribution', models.DateField(default=datetime.date.today)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
