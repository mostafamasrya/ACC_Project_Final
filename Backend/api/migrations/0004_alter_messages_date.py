# Generated by Django 4.0.5 on 2022-07-22 23:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_messages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 2, 6, 16, 908024)),
        ),
    ]
