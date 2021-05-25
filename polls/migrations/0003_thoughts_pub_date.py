# Generated by Django 3.1.6 on 2021-02-09 22:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_thoughts'),
    ]

    operations = [
        migrations.AddField(
            model_name='thoughts',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 22, 45, 37, 811235, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
