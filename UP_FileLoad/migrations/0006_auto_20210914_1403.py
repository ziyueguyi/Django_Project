# Generated by Django 3.2.7 on 2021-09-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UP_FileLoad', '0005_auto_20210914_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='files_info',
            name='md5_fn',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
