# Generated by Django 3.1 on 2023-11-27 21:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20231127_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 143155, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 143176, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 141510, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 141535, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 139521, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 143643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 143663, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clients',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 146215, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clients',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 146237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 140024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 140052, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 145192, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 145213, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 142649, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 142677, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 141016, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 141037, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 140528, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 140550, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 141989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 142009, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 144192, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 144212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 144694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 39, 10, 144722, tzinfo=utc)),
        ),
    ]
