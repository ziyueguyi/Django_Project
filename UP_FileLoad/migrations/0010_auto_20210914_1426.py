# Generated by Django 3.2.7 on 2021-09-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UP_FileLoad', '0009_auto_20210914_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files_info',
            name='file_name',
        ),
        migrations.AddField(
            model_name='files_info',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files_info',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
