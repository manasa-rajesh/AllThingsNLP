# Generated by Django 3.0.4 on 2021-09-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_summarization', '0002_auto_20210914_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesupload',
            name='id',
        ),
        migrations.AddField(
            model_name='filesupload',
            name='file_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filesupload',
            name='ids',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
