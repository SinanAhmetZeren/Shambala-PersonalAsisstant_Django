# Generated by Django 3.1.7 on 2021-04-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measures',
            name='measure_3',
            field=models.IntegerField(default=0, verbose_name='measure 3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measures',
            name='measure_4',
            field=models.IntegerField(default=0, verbose_name='measure 4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measures',
            name='measure_5',
            field=models.IntegerField(default=0, verbose_name='measure 5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measures',
            name='measure_6',
            field=models.IntegerField(default=0, verbose_name='measure 6'),
            preserve_default=False,
        ),
    ]
