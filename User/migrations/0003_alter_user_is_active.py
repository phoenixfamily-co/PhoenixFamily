# Generated by Django 4.2.16 on 2025-02-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_is_verified_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال'),
        ),
    ]
