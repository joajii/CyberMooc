# Generated by Django 5.1.4 on 2024-12-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyberapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
