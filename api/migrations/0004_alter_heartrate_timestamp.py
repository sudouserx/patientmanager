# Generated by Django 5.1.6 on 2025-02-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartrate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
