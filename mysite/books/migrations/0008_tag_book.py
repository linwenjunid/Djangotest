# Generated by Django 2.1.4 on 2019-01-09 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_book_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='关键字'),
        ),
    ]
