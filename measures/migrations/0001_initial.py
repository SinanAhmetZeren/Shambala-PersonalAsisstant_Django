# Generated by Django 3.1.7 on 2021-04-19 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='measures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_1', models.IntegerField(verbose_name='measure 1')),
                ('measure_2', models.IntegerField(verbose_name='measure 2')),
                ('measure_date', models.DateField(verbose_name='measure date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='measure input date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
