# Generated by Django 2.1.4 on 2019-01-09 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190109_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
    ]