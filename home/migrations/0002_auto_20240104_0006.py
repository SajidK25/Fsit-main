# Generated by Django 3.1 on 2024-01-04 00:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 998788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 998834, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 5564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 5609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 6672, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 6718, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 995246, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 995307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 990857, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 999909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 999962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 992156, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 992202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 3357, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 3402, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 997535, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 997580, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 994213, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 994259, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 993170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 993217, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 996366, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 50, 996412, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 1024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 1069, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 2273, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 6, 51, 2343, tzinfo=utc)),
        ),
    ]