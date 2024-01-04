# Generated by Django 3.1 on 2024-01-04 00:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeedHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(help_text='+92-0900-10072', max_length=15)),
                ('address', models.CharField(blank=True, help_text='address', max_length=256, null=True)),
                ('city', models.CharField(blank=True, help_text='city', max_length=256, null=True)),
                ('country', models.CharField(blank=True, help_text='country', max_length=256, null=True)),
                ('open_time', models.CharField(blank=True, help_text='time', max_length=256, null=True)),
                ('closed', models.CharField(blank=True, help_text='time', max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicesdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 469666, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 469736, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 468425, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 468470, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QualityAssurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 463607, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 463651, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 460506, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 460551, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 461533, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 461578, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 464830, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 464875, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 470775, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 470821, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 459236, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 459281, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 467269, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 467314, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessToNext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 457580, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 462533, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 462592, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blogsdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 474119, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 474166, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 473003, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 473048, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 466200, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(default=datetime.datetime(2024, 1, 4, 0, 1, 36, 466245, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
