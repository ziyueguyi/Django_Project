# Generated by Django 3.2.7 on 2021-09-14 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UP_FileLoad', '0017_auto_20210914_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='files_info',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files_info',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='files_info',
            name='ip_address',
            field=models.GenericIPAddressField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files_info',
            name='machine_code',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files_info',
            name='md5_fn',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files_info',
            name='state',
            field=models.BooleanField(default=1),
        ),
    ]
