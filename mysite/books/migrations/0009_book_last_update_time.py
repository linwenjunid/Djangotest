# Generated by Django 2.1.4 on 2019-01-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_tag_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='last_update_time',
            field=models.DateField(auto_now=True, verbose_name='出版日期'),
        ),
    ]
