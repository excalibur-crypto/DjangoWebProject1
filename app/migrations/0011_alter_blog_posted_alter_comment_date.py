# Generated by Django 5.1.2 on 2024-11-14 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_blog_posted_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 14, 19, 24, 25, 448266), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 14, 19, 24, 25, 448266), verbose_name='Дата комментария'),
        ),
    ]
