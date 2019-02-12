# Generated by Django 2.1.4 on 2019-01-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='关键字')),
            ],
            options={
                'verbose_name': '关键字',
                'verbose_name_plural': '关键字',
                'ordering': ['tag'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.Tag', verbose_name='关键字'),
        ),
    ]