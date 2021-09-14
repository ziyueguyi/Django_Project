# Generated by Django 3.2.7 on 2021-09-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UP_FileLoad', '0024_files_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='files_info',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files_info',
            name='file_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
