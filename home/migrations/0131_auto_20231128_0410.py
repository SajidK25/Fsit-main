# Generated by Django 3.1 on 2023-11-28 04:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0130_auto_20231128_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 102391, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 102411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 100651, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 100679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 98664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 102919, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 102940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clients',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 105421, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clients',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 105443, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 99164, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 99186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 104398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 104420, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 101897, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 101922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 100163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 100184, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 99670, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 99692, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 101276, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 101299, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 103409, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 103429, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 103902, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 4, 10, 47, 103929, tzinfo=utc)),
        ),
    ]
