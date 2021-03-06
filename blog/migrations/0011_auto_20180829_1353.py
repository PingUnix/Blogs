# Generated by Django 2.1 on 2018-08-29 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20180829_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='VIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vipuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('41dcacfa-39f7-4db1-916d-5d539dda0002'), help_text='id for comment', primary_key=True, serialize=False),
        ),
    ]
