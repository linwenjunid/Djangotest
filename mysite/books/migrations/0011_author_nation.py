# Generated by Django 2.1.4 on 2019-01-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20190109_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nation',
            field=models.CharField(default='中国', max_length=20, verbose_name='国籍'),
        ),
    ]
