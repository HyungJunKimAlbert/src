# Generated by Django 2.2.1 on 2020-04-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200426_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
