# Generated by Django 3.2.7 on 2021-09-14 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UP_FileLoad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files_info',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='files_info',
            name='machine_code',
        ),
    ]
