# Generated by Django 5.1.2 on 2024-10-27 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 10, 27, 13, 40, 19, 620373), verbose_name='Опубликована'),
        ),
    ]