# Generated by Django 3.1.7 on 2021-04-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0003_setmeasures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setmeasures',
            name='measure_1_name',
            field=models.CharField(max_length=20, verbose_name='measure 1'),
        ),
        migrations.AlterField(
            model_name='setmeasures',
            name='measure_2_name',
            field=models.CharField(max_length=20, verbose_name='measure 2'),
        ),
        migrations.AlterField(
            model_name='setmeasures',
            name='measure_3_name',
            field=models.CharField(max_length=20, verbose_name='measure 3'),
        ),
        migrations.AlterField(
            model_name='setmeasures',
            name='measure_4_name',
            field=models.CharField(max_length=20, verbose_name='measure 4'),
        ),
        migrations.AlterField(
            model_name='setmeasures',
            name='measure_5_name',
            field=models.CharField(max_length=20, verbose_name='measure 5'),
        ),
        migrations.AlterField(
            model_name='setmeasures',
            name='measure_6_name',
            field=models.CharField(max_length=20, verbose_name='measure 6'),
        ),
    ]
