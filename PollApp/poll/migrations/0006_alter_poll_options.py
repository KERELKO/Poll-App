# Generated by Django 5.0.1 on 2024-02-09 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_remove_poll_date_to_close_remove_poll_is_closed_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'ordering': ['created']},
        ),
    ]
