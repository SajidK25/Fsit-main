# Generated by Django 3.1 on 2024-01-04 00:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240104_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 515161, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 515186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 519010, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 519035, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 519634, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 519659, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 513241, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 513279, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 510743, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 515773, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 515797, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 511466, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 511491, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 517779, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 517804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 514460, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 514485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 512660, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 512684, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 512064, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 512089, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 513861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 513886, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 516436, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 516460, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 517161, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 42, 20, 517201, tzinfo=utc)),
        ),
    ]
