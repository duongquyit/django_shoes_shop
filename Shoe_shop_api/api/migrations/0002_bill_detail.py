# Generated by Django 4.0.4 on 2022-06-01 06:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_Detail',
            fields=[
                ('bill_detais_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bill')),
            ],
        ),
    ]
