# Generated by Django 3.2.7 on 2021-09-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UP_FileLoad', '0011_auto_20210914_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files_info',
            name='state',
        ),
        migrations.AddField(
            model_name='files_info',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]