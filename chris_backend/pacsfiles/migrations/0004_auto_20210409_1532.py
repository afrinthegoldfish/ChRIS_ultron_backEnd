# Generated by Django 2.2.12 on 2021-04-09 19:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pacsfiles', '0003_pacsfile_modality'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacsfile',
            name='ProtocolName',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='pacsfile',
            name='StudyDate',
            field=models.DateField(db_index=True, default=datetime.datetime(2021, 4, 9, 19, 32, 14, 90971, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='SeriesInstanceUID',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='pacsfile',
            name='StudyInstanceUID',
            field=models.CharField(max_length=150),
        ),
    ]