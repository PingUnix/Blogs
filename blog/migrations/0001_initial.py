# Generated by Django 2.1 on 2018-08-29 00:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('contents', models.CharField(max_length=65535)),
                ('publish_date', models.DateField(blank=True, default=datetime.date(2018, 8, 29), null=True)),
                ('blogger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('3291c74f-5492-4e89-9e9c-0f1852740715'), help_text='id for comment', primary_key=True, serialize=False)),
                ('contents', models.CharField(max_length=1000)),
                ('comment_date', models.DateField(blank=True, default=datetime.date(2018, 8, 29), null=True)),
                ('status', models.CharField(blank=True, choices=[('c', 'censorship'), ('p', 'published')], default='c', help_text='status of comments', max_length=1)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blog')),
                ('commentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['comment_date'],
            },
        ),
    ]
