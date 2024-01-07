# Generated by Django 3.1 on 2024-01-05 18:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240104_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 983893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 983925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 989763, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 989788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 990400, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 990425, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 981152, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 981211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 976802, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 984520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 984544, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 978062, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 978106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 988526, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 988551, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 983178, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 983202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 980122, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 980166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 979043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 979087, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 982198, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 982242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 986752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 986775, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 987459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 18, 19, 46, 987498, tzinfo=utc)),
        ),
    ]