# Generated by Django 3.1.7 on 2021-04-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0004_auto_20210420_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setmeasures',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
