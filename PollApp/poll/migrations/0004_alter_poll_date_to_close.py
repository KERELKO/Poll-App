# Generated by Django 5.0.1 on 2024-02-04 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_choice_user_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_to_close',
            field=models.DurationField(default=datetime.timedelta(days=2)),
        ),
    ]