# Generated by Django 3.1 on 2021-01-01 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210101_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 389564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 389564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 388565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 388565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 386572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 390564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 390564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 386572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 386572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 392555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 392555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 389564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 389564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 387568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 387568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 387568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 387568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 388565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 388565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 391558, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 391558, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 391558, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 21, 20, 391558, tzinfo=utc)),
        ),
    ]
