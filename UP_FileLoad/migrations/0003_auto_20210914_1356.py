# Generated by Django 3.2.7 on 2021-09-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UP_FileLoad', '0002_auto_20210914_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files_info',
            name='id',
        ),
        migrations.AddField(
            model_name='files_info',
            name='file_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='files_info',
            name='ip_address',
            field=models.CharField(default='127.0.0.1', max_length=32),
        ),
        migrations.AddField(
            model_name='files_info',
            name='machine_code',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='files_info',
            name='md5_fn',
            field=models.CharField(default=None, max_length=64, primary_key=True, serialize=False),
        ),
    ]
