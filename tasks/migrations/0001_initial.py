# Generated by Django 4.0.5 on 2022-06-26 21:23

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(auto_now_add=True)),
                ('date_end', models.DateField(default=datetime.datetime(2022, 6, 26, 21, 23, 23, 475506, tzinfo=utc))),
                ('text', models.CharField(max_length=50)),
                ('finished', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]