# Generated by Django 3.1.7 on 2021-04-19 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('measures', '0002_auto_20210420_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='setmeasures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_1_name', models.IntegerField(verbose_name='measure 1')),
                ('measure_2_name', models.IntegerField(verbose_name='measure 2')),
                ('measure_3_name', models.IntegerField(verbose_name='measure 3')),
                ('measure_4_name', models.IntegerField(verbose_name='measure 4')),
                ('measure_5_name', models.IntegerField(verbose_name='measure 5')),
                ('measure_6_name', models.IntegerField(verbose_name='measure 6')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]