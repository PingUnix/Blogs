# Generated by Django 2.1 on 2018-08-29 19:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180829_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogauthor',
            options={'permissions': (('can_access_author', 'see all bloggers list'),)},
        ),
        migrations.AlterField(
            model_name='blogauthor',
            name='bio',
            field=models.TextField(help_text='input the detail here', max_length=516),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('390a2e01-43ac-4222-b896-b04cdd1324b8'), help_text='id for comment', primary_key=True, serialize=False),
        ),
    ]