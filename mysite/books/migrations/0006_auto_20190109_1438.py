# Generated by Django 2.1.4 on 2019-01-09 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20190109_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.Tag', verbose_name='关键字'),
        ),
    ]
