# Generated by Django 3.1.7 on 2021-04-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210426_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='youtube_id',
            field=models.CharField(default="f'{self.user.username} Profile'", max_length=50, verbose_name='youtube'),
        ),
    ]
