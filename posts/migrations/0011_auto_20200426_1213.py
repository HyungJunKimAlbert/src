# Generated by Django 2.2.1 on 2020-04-26 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_view_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='view_comment_count',
        ),
    ]
