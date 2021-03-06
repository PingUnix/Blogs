# Generated by Django 2.1 on 2018-08-29 13:59

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180829_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='vip',
            name='join_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ff274c74-3583-4c1d-a680-2ba3506dfee6'), help_text='id for comment', primary_key=True, serialize=False),
        ),
    ]
